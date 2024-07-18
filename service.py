import os
import socket
import time
from data_guard import Validation
from dotenv import dotenv_values
from file_integration import CsvWriter
from logit import get_logger
from process_priority import setpriority
from python_service import PythonService

BASEPATH = os.path.abspath(os.path.dirname(__file__))
LOG_FILE = BASEPATH + '\\data\\service.log'

# Raise process priority level to HIGH priority
setpriority(priority=4)

class BarTenderScannerService(PythonService):

    # Inherited class members
    _svc_name_ = "BarTenderScannerAutomation"
    _svc_display_name_ = "BarTender Scanner Automation Service"
    _svc_description_ = "Bartender and Keyence SR-X100 Scanner automation using file integration and Python sockets."
    _exe_name_ = "C:\Program Files\Python311\Lib\site-packages\win32\pythonservice.exe"
    
    def start(self):
        ''' 
        Interface Method: Override method to set the running conditions
        '''
        os.chdir(BASEPATH)
        self.env = dotenv_values()
        self.log = get_logger(__name__, log_file=LOG_FILE, debug=True)
        self.is_running = True
        self.first_time = True
        self.last_time = time.time()

    def stop(self):
        '''
        Interface Method: 
            Override method to invalidate the running condition 
            when the service is requested to be stopped.
        '''
        self.is_running = False

    def step(self, data):
        ''' The business logic '''
        this_time = time.time()
        debounced = int(this_time - self.last_time) >= 3

        if data and not debounced:
            self.log.warning("Read frequency error: too soon.")

        if data and (self.first_time or debounced):
            self.first_time = False

            self.log.info(f"Received {data!r}")
            
            serial_string = data.decode('utf-8')
            serial_number = serial_string[:14]

            self.log.info(f"Serial to label: {serial_number}")

            # Check and process data
            if Validation.check(serial_number, m_line=self.env["CURRENT_LINE"]):
                self.log.info(f"Data: is valid: {serial_number}")
                
                # Pass data to BarTender File Integration
                CsvWriter.save(data=serial_number, 
                               header=self.env["INTEGRATION_FILE_HEADERNAME"], 
                               file_name=self.env["INTEGRATION_FILENAME"])
                self.log.info(f"Data: saved to integration file")
            else:
                # TODO: Handle incorrect data
                self.log.error(f"Data: scanner read not valid serial number")

            self.last_time = this_time

    # 
    def main(self):
        '''
        Interface Method: Override method to perform the service function
        '''
        self.log.info(f"App started")
        while True:
            if not self.is_running:
                break

            try:
                host = self.env["SCANNER_HOST"]
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.env["SCANNER_HOST"], int(self.env["SCANNER_PORT"])))
                    self.log.info(f"Connected to {host}")
                    data = s.recv(1024)  # NOTE: This is a blocking call
                    self.step(data)

            except Exception as err:
                self.log.error(err)
                self.stop()


# Use this condition to determine the execution context.
if __name__ == '__main__':
    # Handle the command line when run as a script
    BarTenderScannerService.parse_command_line()

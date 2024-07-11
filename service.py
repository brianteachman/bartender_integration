from python_service import PythonService
from main import app
import logging


logging.basicConfig(filename='C:\\bin\\controller\\data\\service.log', encoding='utf-8', level=logging.DEBUG)


class SerialPrinterService(PythonService):

    # Inherited class members
    _svc_name_ = "TraceabilityPrinterService"
    _svc_display_name_ = "Traceability Printer Service"
    _svc_description_ = "Transfer serial number to Bartender REST API using Python sockets."
    _exe_name_ = "C:\Python\Lib\site-packages\win32\pythonservice.exe"
    

    # Override the method to set the running condition
    def start(self):
        self.isrunning = True

    # Override the method to invalidate the running condition 
    # When the service is requested to be stopped.
    def stop(self):
        self.isrunning = False

    # Override the method to perform the service function
    def main(self):

        while self.isrunning:
            try:
                app.run(self.isrunning)
            except Exception as err:
                logging.error(err)
                self.stop()


# Use this condition to determine the execution context.
if __name__ == '__main__':
    # Handle the command line when run as a script
    SerialPrinterService.parse_command_line()

import socket
import time

from data_guard import Validation
from file_integration import CsvWriter

HOST = "10.0.180.201"  # The IP address of the scanner
PORT = 9004  # Port to listen on (non-privileged ports are > 1023)


class MainApp():

    def __init__(self):
        pass

    def step(self):
        ''' The business logic '''
        this_time = time.time()
        # print("Loaded step: " + str(this_time))

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))

            while True:
                data = s.recv(1024)
                if data:
                    print(f"Received {data!r}")
                    
                    # Check and process data
                    if Validation.check(data):
                            
                        # Pass data to BarTender File Integration
                        CsvWriter.save(data)

                    else:
                        # TODO: Handle incorrect data
                        pass

    def run(self, is_running=True):
        ''' Run the business logic in a loop '''
        if is_running:
            self.step()

    def exit(self):
        ''' Shutdown process '''
        pass


app = MainApp()

if __name__ == '__main__':
    app.run()


import socket
import time

from printer import Bartender

HOST = "10.0.180.201"  # The IP address of the scanner
PORT = 9004  # Port to listen on (non-privileged ports are > 1023)


class MainApp():

    def __init__(self):
        self.printer = Bartender()

    def step(self):
        ''' The business logic '''
        this_time = time.time()
        # print("Loaded step: " + str(this_time))

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))

            while True:
                data = s.recv(1024)
                # Process serial data here
                if data:
                    print(f"Received {data!r}")
                    
                    res = self.printer.send(data)
                    if res:
                        print(f"Printer response: {res!r}")

    def run(self, is_running=True):
        ''' Run the business logic in a loop '''
        self.step()

    def exit(self):
        ''' Close COM port '''
        pass


app = MainApp()

if __name__ == '__main__':
    app.run()


import requests

# defining the api-endpoint
API_ROOT_URL = "http://localhost/BarTender"

API_PRINT = API_ROOT_URL + "/api/v1/print"
API_AUTH = API_ROOT_URL + "/api/v1/Authenticate"


class Bartender():

    def __init__(self):
        pass

    def pack(self, data):
        post_data = {
            'PrintBTWAction': {
                "Document": "C:\\Templates\\L7_SerialLabel",
                "Printer": "CAB XX.XXX ... (300 dpi)",
                "SaveAfterPrint": False,
                "Copies": 1,
                "VerifyPrintJobComplete": True,
                "NamedDataSource": {
                    "Serial-Number": data
                    }
                }
            }
            
    def send(self, serial_number):
        # sending post request and saving response as response object
        response = requests.post(url=API_PRINT, data=self.pack(serial_number))

        return response.text


# CAB Printer Automation using Bartender

## Setup environment

Install dependancies:

    python -m pip install -r requirements.txt

Wherever the pywin32 library installed to, run the pywin32_postinstall.py script. Like so:

    python "C:\Program Files\Python311\Scripts\pywin32_postinstall.py" -install

Create '.env' file in the root project directory:

    CURRENT_LINE = '07'  # 2 Digit line number
    SCANNER_HOST = "XXX.XXX.XXX.XXX"  # The IP address of the scanner
    SCANNER_PORT = XXXX  # Port to listen on (non-privileged ports are > 1023)
    INTEGRATION_FILENAME = 'C:\\data.csv'  # Where integration file is to be written
    INTEGRATION_FILE_HEADERNAME = 'SerialNumber'  # CSV integration file header name


Create 'service.log' file in the data directory:

    PROJECT_DIRECTORY\data\service.log

## Setup Windows Service

Install service: 

    > python service.py --startup=auto install

Service should be set to start when windows starts. Verify in the Windows 'Services' interface.

Manage Service:

    > python service.py debug
    > python service.py update
    > python service.py start
    > python service.py stop
    > python service.py remove
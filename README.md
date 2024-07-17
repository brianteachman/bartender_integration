# CAB Printer Automation using Bartender

## Setup environment

python -m venv venv
./venv/Scripts/Activate.ps1

python -m pip install -r requirements.txt


## Create Windows Service

    > python service.py --startup=auto install
    
    > python "C:\Program Files\Python311\Scripts\pywin32_postinstall.py" -install

    > python service.py remove
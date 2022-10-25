import logging
import os
from pathlib import Path
import logging

package_name = "bank_marketing_data_EDA"

list_of_file = [

    'requirements.txt',
    'research.py',
    'bank_marketing_EDA.ipynb'
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir  != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating direcotry: {filedir} for file : {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass # create an empy file
            logging.info(f"Creating empy file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")


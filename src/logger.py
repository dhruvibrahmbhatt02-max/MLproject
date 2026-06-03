# check documentation
# basically logging all the information which is executing in every file
# errors and exceptions also gets logged
import logging
import os
from datetime import datetime

# path where all the log file will be stored
LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
# path where log files will be saved
logs_path=os.path.join(os.getcwd(),"logs")
# make dir if not exitst
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

'''if __name__=='__main__':
    logging.info("logging has started")
    raise Exception("just for checking exception handling")
'''
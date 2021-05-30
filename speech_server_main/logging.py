import os
from os import path
import logging
from speech_server_main.config import config

if not path.exists("./logs"):
    os.mkdir("./logs")
    
logging.basicConfig(filename="./logs/deepspeech_server.log", format='%(levelname)s %(asctime)s %(message)s')
def log(message, log_level="warning"):
    
    set_debug = config.ConfigDeepSpeech().get_config("debug")
    if set_debug == "1":
        logging.getLogger(None).setLevel(logging.DEBUG)
    if log_level == "debug":
        logging.debug(message)
    elif log_level == "info":
        logging.info(message)
    elif log_level == "error":
        logging.error(message)
    else:
        logging.warning(message)
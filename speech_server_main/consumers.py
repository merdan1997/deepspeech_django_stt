'''
Channel consumers
'''

from datetime import datetime
from speech_server_main.config import config
from .deepspeech import deepspeech as ds
import os, re

conf = config.ConfigDeepSpeech()

audiofiledir = conf.get_config('audiofiledir')
def ws_connect(message):
    # Accept the incoming connection
    message.reply_channel.send({"accept": True})
    print('websocket connected')

def ws_message(message):
    print('ws message received')
    file_name = audiofiledir + 'ws_generated' + datetime.now().strftime('%y-%m-%d_%H%M%S')
    with open(file_name, 'wb') as fp:
        fp.write(message.content['bytes'])
        fp.flush()
    msg = ds.stt(file_name, True)
    message.reply_channel.send({'text':msg})

def ws_disconnect(message):
    print('ws disconnected')
    delete_files_in_dir('^ws_generated', audiofiledir)

def delete_files_in_dir(pattern, dir):
    print('inside delete module')
    for file in os.listdir(dir):
        if re.search(pattern, file):
            os.remove(os.path.join(dir, file))

DeepSpeech Django STT Server API
==========================
This is an API which is used as a backend of DeepSpeech that allow developers to converting audio data (wav) being transfered through the API and return response and handles the process of the converting audio into text from the model with best accuracy.

## Installation
Download or clone this project. This project uses python3. To run this project you need to first install deepspeech's model and scorer. Check out [deepspeech's README.md](https://github.com/mozilla/DeepSpeech/blob/master/README.rst) for details on how to install deepspeech on your machine. Then copy both to dsmodel folder and put path for both file in the correct point in config.json.
    
Once deepspeech's materials is installed, run the following commend line to install vitualenv:

    pip3 install virtualenv

Build virtual environment for the local directory

    python -m venv "env"

Activate virtual environment
## Ubuntu

    source env/bins/activate

## Window

    env\Scripts\activate

 Moreover, Create audio folder to store saved byte file and put the path in the config.json. Then run following command to install required dependencies of **django-deepspeech-server:**

    pip3 install -r path/to/django-deepspeech-server/requirements.txt

## Configuration
Don't forget to put path in the config.json for the following file, Also make change to **audiofiledir** key in same config.json file, to match some valid path on your system.

Go to directory where manage.py is located and start server:

    python3 manage.py runserver
    
Go to your browser and browse to http://127.0.0.1:8000/dsserver.
Alternatively, you can use use https server, using below command:

    python3 manage.py runsslserver

Now you can access website over https (https://127.0.0.1:8000).


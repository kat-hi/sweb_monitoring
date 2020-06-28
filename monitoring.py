from datetime import datetime
from .mail import log_into_SMTP_Server_and_send_email
import requests
import os

STATE = 1

def request_map():
    global STATE
    URL = os.environ.get('URL')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('REQUEST MAP: | {}'.format(dt_string))
    response = requests.get(URL)
    print('STATUS CODE: | {}'.format(response))
    if response.status_code != 200 and STATE == 1:
        '''
        a new error occurs. state 1 does not match with a 200 response.
        email with error code will be send to the admin
        '''
        STATE = 0
        log_into_SMTP_Server_and_send_email(response.status_code)
    elif response.status_code == 200 and STATE == 0:
        '''
        an error is solved. the old (error-)State was 0 and now there is a 200 response.
        email with the message "error solved" will be send to the admin
        '''
        STATE = 1
        email_text = 'error solved: {}'.format(response.status_code)
        log_into_SMTP_Server_and_send_email(email_text)
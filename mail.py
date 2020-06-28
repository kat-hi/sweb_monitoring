from _socket import gaierror
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
import os

PORT = os.environ.get('PORT')
SERVER = os.environ.get('SERVER')
SENDER = os.environ.get('SENDER')
RECEIVER = os.environ.get('RECEIVER')
PASSWORD = os.environ.get('PASSWORD')


def log_into_SMTP_Server_and_send_email(emailtext):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Api Error"
    message["From"] = RECEIVER
    message["To"] = RECEIVER
    part1 = MIMEText(str(emailtext), "plain")
    message.attach(part1)
    context = ssl.create_default_context()

    try:
        print('try to log into SMTP-Server')
        with smtplib.SMTP_SSL(SERVER, PORT, context=context) as server:
            server.login(SENDER, PASSWORD)
            print('connected with SMTP-Serverr')
            server.sendmail(SENDER, RECEIVER, message.as_string())
            print('email sent')
    except (gaierror, ConnectionRefusedError):
        print('Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: {}'.format(e))
    else:
        print('Sent')

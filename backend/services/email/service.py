from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
import config

# Configuration
port = config.emailService["port"]
smtp_server = config.emailService["smtp_server"]
login = config.emailService["login"]
password = config.emailService["password"]
sender_email = config.emailService["sender_email"]
receiver_email = ""

def SEND_COMF(_email, _text):
    receiver_email = _email
    # message = MIMEText(_text, "plain")
    message = MIMEText(_text, 'html')
    # message = MIMEMultipart('alternative' ,_text)
    message["Subject"] = "Confirmation email Game Play platform maximumroulette.com"
    message["From"] = sender_email
    message["To"] = receiver_email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('Sent email ok2.')

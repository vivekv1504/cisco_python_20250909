import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .config import Config

from_address = Config.MAIL_USERNAME
app_password = Config.MAIL_PASSWORD
to_address = Config.NOTIFICATION_EMAIL

def send_gmail(to_address, subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = from_address
        msg["To"] = to_address
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_address, app_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print("Error while sending email:", e)
        return False

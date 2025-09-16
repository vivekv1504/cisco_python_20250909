import threading
from flask_mail import Message
from flask import current_app
from .extensions import mail  # import mail here to avoid circular import

def send_email(msg):
    with current_app.app_context():
        mail.send(msg)

def notify_account_creation(account):
    subject = "Account Created"
    body = f"Account '{account.name}' with number {account.number} has been created with balance {account.balance}."
    msg = Message(subject, recipients=[current_app.config.get("MAIL_USERNAME")], body=body)
    thread = threading.Thread(target=send_email, args=(msg,))
    thread.start()

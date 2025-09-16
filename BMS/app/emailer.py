import threading
from flask import current_app
from .mail_send import send_gmail

def notify_account_creation(account):
    subject = "Account Created Successfully"
    body = (
        f"Hello {account.name},\n\n"
        f"Your account with number {account.number} has been successfully created.\n"
        f"Current balance: {account.balance}\n\n"
        "Thank you for using our service."
    )

    to_address = current_app.config.get('NOTIFICATION_EMAIL', 'vinthavivekreddy@gmail.com')

    def send_email_async():
        success = send_gmail(to_address, subject, body)
        if not success:
            current_app.logger.error("Failed to send account creation email")

    thread = threading.Thread(target=send_email_async)
    thread.start()



'''import threading
from flask_mail import Message
from flask import current_app
from .extensions import mail  # import mail here to avoid circular import

def send_email(msg):
    with current_app.app_context():
        mail.send(msg)

def notify_account_creation(account):
    subject = "Account Created"
    body = (f"Hello {account.name},\n\n"
        f"Your account with number {account.number} has been successfully created.\n"
        f"Current balance: {account.balance}\n\n"
        "Thank you for using our service." )
    sender = current_app.config.get('MAIL_DEFAULT_SENDER', current_app.config.get('MAIL_USERNAME'))
    to_address = current_app.config.get('NOTIFICATION_EMAIL')
    msg = Message(subject, recipients=["vinthavivekreddy@gmail.com"], body=body)
    #send_email(msg)
    #thread = threading.Thread(target=lambda: mail.send(msg))
    #thread.start()
    '''

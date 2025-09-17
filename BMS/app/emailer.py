import threading
from flask import current_app
from .mail_send import send_gmail

def notify_account_creation(account):
    """notify_account_creation(account):
    Sends an email notification asynchronously to notify that 
    a new account has been successfully created. Uses SMTP 
    credentials and sends email in a separate thread to avoid 
    blocking HTTP requests."""
    subject = "Account Created Successfully"
    """The email contains:
- The account holder's name,
- Account number,
- Current balance,
- A thank you message."""
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
    """Threading:
- Email sending runs in a background thread to improve API response time"""
    thread = threading.Thread(target=send_email_async)
    thread.start()



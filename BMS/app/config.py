import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'vinthavivek19@gmail.com'               # Your sender email
    MAIL_PASSWORD = 'lzwdmxzzdqioumgi'                      # Your app password
    MAIL_DEFAULT_SENDER = 'vinthavivek19@gmail.com'         # Must be set to avoid sender error

    NOTIFICATION_EMAIL = 'vinthavivekreddy@gmail.com'       # Receiver email

    BATCH_SIZE = int(os.getenv('BATCH_SIZE', 10))
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')



'''import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME','vinthavivek19@gmail.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    NOTIFICATION_EMAIL = os.getenv('NOTIFICATION_EMAIL', 'prabhasavvari24@gmail.com')
    BATCH_SIZE = int(os.getenv('BATCH_SIZE', 10))
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')'''

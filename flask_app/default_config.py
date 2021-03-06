#Logging
LOG_FILE_LOC = 'flask_app/logs/error.log'

#Database
DB_USERNAME = ''
DB_PASSWORD = ''
DB_SERVER = ''
DB_NAME = ''

#Secret keys
SECRET_KEY = ''
SECRET_KEY_HASH = ''

#Mail settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
SENDER_EMAIL = ''

#Flask
DEBUG = True

#Celery
BROKER_URL = 'sqla+mysql://scott:tiger@localhost/scott'
CELERY_RESULT_BACKEND = "database"
CELERY_RESULT_DBURI = "mysql://scott:tiger@localhost/scott"

#FLASK-SECURITY CONFIG
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_RECOVERABLE = True
SECURITY_LOGIN_WITHOUT_CONFIRMATION = False #True
SECURITY_PASSWORD_HASH = "bcrypt"
SECURITY_PASSWORD_SALT = "jawjdn9203skmd"
SECURITY_EMAIL_SENDER = ""

#Recaptcha
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = "6Lcgj-ASAAAAAI7PXbP29Sx0D7WmnKSX9RtI93Bi"
RECAPTCHA_PRIVATE_KEY = "6Lcgj-ASAAAAACt5N1sNgPTYRJ6na3NDqhlrUf_t"
#RECAPTCHA_OPTIONS


#Pending : Put IMP keys in environment variables.


class Config:
    SECRET_KEY = 'c21465221d58bcacf79f30d8cee9f55a'
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'akashmali8599@gmail.com'
    MAIL_PASSWORD = 'Akya@101320'

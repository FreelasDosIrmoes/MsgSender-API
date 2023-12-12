import os

from flask import *
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

mail_server = os.getenv('MAIL_SERVER')
mail_port = os.getenv('MAIL_PORT')
mail_username = os.getenv('MAIL_USERNAME')
mail_password = os.getenv('MAIL_PASSWORD')

app_flask = Flask(__name__)
app_flask.config['MAIL_SERVER'] = mail_server
app_flask.config['MAIL_PORT'] = mail_port  # Porta do servidor SMTP
app_flask.config['MAIL_USE_TLS'] = True  # Use TLS para criptografia
app_flask.config['MAIL_USERNAME'] = mail_username
app_flask.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app_flask)
from app import views
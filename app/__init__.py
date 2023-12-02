from flask import *
import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from app.service import *


load_dotenv()
KEY = os.getenv('API_KEY')

app = Flask(__name__)

from app import views
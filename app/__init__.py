from flask import *
from flask_migrate import Migrate
from app.service import *


app_flask = Flask(__name__)

from app import views
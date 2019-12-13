from flask import Flask

from .config import app_config
from .models import db, bcrypt

# import user_api blueprint
from .views.UserView import user_api as user_blueprint
from .views.BlogpostView import blogpost_api as blogpost_blueprint



app = Flask(__name__)

@app.route('/')
def index():
    return 'Congratulations! Your part 2 endpoint is working'



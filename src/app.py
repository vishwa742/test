#src/app.py

from flask import Flask

from .config import app_config
from .models import db, bcrypt

# import user_api blueprint
from .views.UserView import user_api as user_blueprint
from .views.BlogpostView import blogpost_api as blogpost_blueprint

#app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
#app.register_blueprint(blogpost_blueprint, url_prefix='/api/v1/blogposts')

  # app initiliazation
app = Flask(__name__)

@app.route('/')
def index():
    return 'Congratulations! Your part 3 endpoint is working'
#app.config.from_object(app_config[env_name])

# initializing bcrypt and db
# bcrypt.init_app(app)
#  db.init_app(app)



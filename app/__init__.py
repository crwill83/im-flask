from flask import Flask
from config import Config

# import our blueprints
from .auth.routes import auth
from .ig.routes import ig

# import our db related
from .models import db, User
from flask_migrate import Migrate
from flask_login import LoginManager

# API CROSS ORIGIN IMPORT
from flask_cors import CORS


app  = Flask(__name__)
login = LoginManager()
CORS(app)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(auth)
app.register_blueprint(ig)

app.config.from_object(Config)

# initialize our database to work with our app
db.init_app(app)
login.init_app(app)

login.login_view = "auth.logMeIn"

migrate = Migrate(app, db)

from . import routes
from . import models
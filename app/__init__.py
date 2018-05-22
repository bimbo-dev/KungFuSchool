from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# configure Blueprints
from .views import home, finance
app.register_blueprint(home)
app.register_blueprint(finance)


from app import models
from app.models import seeds



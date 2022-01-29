# Where the app is initialized


from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

# Initializing the application
app = Flask(__name__, instance_relative_config = True)


# Setting up the app configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


# Initializing Flask Extensions
bootstrap = Bootstrap(app)


from app import views
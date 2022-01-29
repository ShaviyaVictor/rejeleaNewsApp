# Where the app is initialized


from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig,config_options


# Initializing Flask Extensions
bootstrap = Bootstrap()

def createApp(config_name) :

  # Initializing the application
  app = Flask(__name__)

  # Setting up the app configuration
  app.config.from_object(config_options[config_name])

  # Initializing flask extensions
  bootstrap.init_app(app)


  # Adding the views and the error by registering the blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)


  return app




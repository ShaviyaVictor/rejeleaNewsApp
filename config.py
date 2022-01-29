# Contains our app configurations
import os

class Config :
  '''
  General configuration parent class
  '''



class ProdConfig(Config) :
  '''
  Production configuration child class
  
  Args:
    Config: The parent configuration class with General configuration settings
  '''
  pass



class DevConfig(Config) :
  '''
  Development configuration child class

  Args:
    Config: The parent configuration class with General configuration settings
  '''


config_options = {
  'development' : DevConfig,
  'production' : ProdConfig
}
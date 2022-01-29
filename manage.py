# File that runs our application


from app import createApp
from flask_script import Manager, Server



# Creating app instance
app = createApp('development')
manager = Manager(app)
manager.add_command('server', Server)

if __name__ == '__main__' :
  main.run()
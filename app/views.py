# Contains all our view functions


from flask import render_template
from app import app
from newsapi import NewsApiClient


# Views
@app.route('/')
def index() :
  '''
  View root page function that returns the index page and its data
  '''

  title = 'Rejelea - Where updates find you.'

  return render_template('index.html', title = title)
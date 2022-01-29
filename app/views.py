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

  newsapi = NewsApiClient(api_key='MOVIE_API_KEY')

  # Getting top headlines
  topHeadlines = newsapi.get_top_headlines(sources='bbc-news')


  title = 'Rejelea - Where updates find you.'

  return render_template('index.html', title = title)
# Contains all our view functions


from flask import render_template
from app import app
from newsapi import NewsApiClient
from instance.config import NEWS_API_KEY



# Views
@app.route('/')
def index() :
  '''
  View root page function that returns the index page and its data
  '''

  newsapi = NewsApiClient(api_key = NEWS_API_KEY)

  # Getting top headlines
  topHeadlines = newsapi.get_top_headlines(sources='bbc-news')

  # Fetching all the articles from the headline news
  allArticles = topHeadlines['articles']

  # Make a list of contents to store the values of my fetched data
  img = []
  url = []
  dated = []
  title = []
  description = []

  # Fetch all contents using the for loop
  for i in range(len(allArticles)) :
    mainArticle = allArticles[i]

    #  Append all the contents to their respective list holders
    title.append(mainArticle['title'])
    description.append(mainArticle['description'])
    img.append(mainArticle['urlToImage'])
    url.append(mainArticle['url'])
    dated.append(mainArticle['publishedAt'])

    # Create a zip for finding the contents directly and faster
    content = zip(title,description,img,url,dated)



  title = 'Rejelea - Where updates find you.'

  return render_template('index.html', title = title, content = content)
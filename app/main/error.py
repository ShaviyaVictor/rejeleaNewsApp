# Contains handlers for error pages

from flask import render_template
from . import main


@main.errorhandler(404)
def fourOwFour(error) :
  '''
  Function to render the 404 error page
  '''
  return render_template('fourOwFour.html'), 404
"""
*
* wordcount.py
* Author:
* Renato Jensen Filho
* 2020-02-11
*
"""

# imports
from flask import Flask, render_template, request
import re


def count_words(s):
  return(len(re.findall(r'[\w]+', s)))

#
# Flask routines
#


# initializes flask application
application = Flask(__name__)


@application.route('/')
def index():
  return render_template("index.html", label="Waiting for some words...")


# count words
@application.route('/', methods=['POST'])
def count():
  if request.method == 'POST':
    text_input = str(request.form['text_input'])

  return render_template('index.html', label='Words counted: '
                         + str(count_words(text_input)))


if __name__ == "__main__":
  application.run()

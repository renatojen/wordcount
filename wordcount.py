"""
* 
* wordcount.py
* Author:
* Renato Jensen Filho
* 2020-02-11
* 
"""

#imports
from flask import Flask, render_template, request
from flask_sslify import SSLify
import re

ssl = False

def count_words(s):
  count = 0
  s = re.sub(r'[^\w]+', ' ', s)
  s = s.strip(' ')
  if len(s) == 0:
    return 0
  for i in s:
    if i == ' ':
      count += 1
  return count+1
    
#
# Flask routines
#

#initializes flask application      
application=Flask(__name__)
if ssl:
  sslify = SSLify(application)

@application.route('/')
def index():        
   return render_template("index.html", label="Waiting for some words...")
  
#count images
@application.route('/', methods=['POST'])
def count():
   if request.method == 'POST':
      text_input = str(request.form['text_input'])
              
   return render_template('index.html', label='Words counted: ' + str(count_words(text_input)))           

if __name__=="__main__":
   application.run()
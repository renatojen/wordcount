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
#from os import remove, listdir, getenv
#from os.path import join, dirname
from datetime import datetime
#from time import time
import re

dt = str(datetime.now())[:-5].replace(' ', '_').replace(':', '').replace('.', '') #YYYY-mm-DD_HHMMSSS   
vr = None
ts = None

def count_words(s):
  count = 0
  #print(s)
  #s = re.sub(r'[ .,/?|:;~˜!@#$%^ˆ&*(){}\'`_=+\-\"\[\]\\\n\r\t]+', ' ', s)
  s = re.sub(r'[^A-Za-z0-9]+', ' ', s)
  #print(s)
  s = s.strip(' ')
  #print(s)
  if len(s) == 0:
    return 0
  for i in s:
    if i == ' ':
      count += 1
  return count+1

#s = " uma \n duas \r tres \t quatro.cinco]seis\\sete/oito,nove.dez?onze!doze#treze$catorze@quize\%dezesseis^dezessete*dezoito&dezenove(vinte)vinteum-vintedois_vintetres+vintequatro=vintecinco"
#print(count_words(s))
 
#initialization
#def init():
#   cfg = safe_load(open("cfg.yml"))
   

#init()
    
#
# Flask routines
#

#initializes flask application      
application=Flask(__name__)

@application.route('/')
def index():        
   return render_template("index.html", label="Waiting for some words...")
  
#classify image, display image and classification results, generate audio results and save image data to database
@application.route('/', methods=['POST'])
def count():
   if request.method == 'POST':
      text_input = str(request.form['text_input'])
              

   return render_template('index.html', label='Words counted: ' + str(count_words(text_input)))           

if __name__=="__main__":
   # Bind to VC_APP PORT/HOST if defined, otherwise default to 5000/localhost.
   #PORT = int(getenv('VCAP_APP_PORT', '5000'))
   #HOST = str(getenv('VCAP_APP_HOST', 'localhost'))
   application.run()
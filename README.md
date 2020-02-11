# Wordcount

<p align="center">
  <img src="http://wordcount.renatojensen.com/static/resources/logo.png">
</p>

You can try a live version of Wordcount here: http://wordcount.renatojensen.com/

## Requirements

Runtime:

* python3

Python packages:

* Click==7.0
* Flask==1.1.1
* itsdangerous==1.1.0
* Jinja2==2.11.1
* MarkupSafe==1.1.1
* Werkzeug==1.0.0

##Usage

Input words and click the "Count!" button. The page will reload itself, displaying the number of words found.

## Run the app locally

To run the app locally you will need:

* python3 runtime
* the app source code

1. Clone wordcount repository
  ```
  $ git clone https://github.com/renatojen/wordcount.git
  ```
  This repository contains all necessary files to run the app locally.

2. Install the required dependencies with pip: in wordcount project folder, run the following command in a command line:
  ```
  $ pip install -r requirements.txt
  ```
  (you might need to use `pip3` command depending on your environment configuration)

3. Run the application:
  ```
  $ python wordcount.py
  ```
  (you might need to use `python3` command depending on your environment configuration)
  
This command will create a new Flask app and start your application. When your app has started, your console will print the following message:

`Running on http://localhost:5000/ (Press CTRL+C to quit)`.

4. Test you application acessing http://localhost:5000/ on your browser.

## Compatibility
Wordcount is compatible with the majority of popular browsers such as Google Chrome, Mozilla Firefox, Opera and mobile devices that supports HTML5.
   
## License
This app is covered by the GNU GENERAL PUBLIC license. For more information, see LICENSE for license information.

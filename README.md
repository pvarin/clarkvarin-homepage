clarkvarin-homepage
===================

A Flask app that serves Clark Varin's homepage.

Flask
-----
For Flask documentation or simply an introduction to Flask visit the [Flask website](http://flask.pocoo.org/ "Flask") 

Testing
-------
To run the server locally type the following command in the root directory:
```
foreman start
```
This should start the server on the default port: [http://0.0.0.0:5000](http://0.0.0.0:5000 "default")

Heroku
------
You can deploy the website to Heroku using the command:
```
git push heroku master
```	

Managing Dependencies
---------------------
This package uses a Python virtualenv to manage dependencies. This means that each time you want to run your app locally you must first load the virtualenv. To do this simply run the command:
```
source venv/bin/activate
```
If you ever need to update the Python dependencies you can type the following command in order to update the requirements.txt file required by Heroku:
```
pip freeze > requirements.txt
```
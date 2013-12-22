import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome to my Website!'
#import application.models
#import application.views
#import application.controllers
import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

app.debug=True

# setup routes
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ideas")
@app.route("/portfolio")
@app.route("/about")
def comming_soon():
	return render_template('comingsoon.html')
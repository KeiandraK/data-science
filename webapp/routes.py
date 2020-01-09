from webapp import app
from flask import render_template


@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/addthis', methods=['GET', 'POST'])
def addthis():
	return f"{10 + 5}"

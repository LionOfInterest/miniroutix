from app import app
from flask import render_template
from flask_cas import login_required

@app.route("/", methods=['GET'])
def home() :
	''' Page d'accueil
	Parameters:
	None

	Returns:
	html: Returns home.html file
	'''
	return render_template('home.html')

@app.route("/coucou/")
def coucou() :
	return "<h1> En cours de ratio </h1>"

@app.route("/dashboard/", methods=['GET'])
@login_required
def dashboard() :
	return render_template("dashboard.html")

from flask_cas import login_required
from app import app
from config import db
import mysql.connector
from flask import render_template
from decouple import config

@app.route("/create/")
@login_required
def create() :
	#Appel d'une fonction pour décoder les informations
	#lancement du script

	#le front devra fournir une barre de prog jolie
	return render_template('create.html')

@app.route("/upgrades/")
@login_required
def upgrade():
	return render_template('upgrades.html')

@app.route("/full_upgrade/")
@login_required
def full_upgrade():
	return render_template('full_upgrade.html')
#check for upgrades and display changelog
#curl -s "https://downloads.openwrt.org/releases/" | grep href | grep -v '(root)' | grep -v KeyCDN | grep -v faillogs | grep -v 'packages-' | sed s/'<\/a>.*'/''/ | sed s/'<tr><td class="n">'/''/ | cut -d'>' -f2 | grep -v '\-rc' | sort | tail -n1
#https://openwrt.org/releases/21.02/notes-21.02.2


@app.route("/devices/", methods=['GET'])
@login_required
def devices():
	dico={}
	liste=[]
	mydb = mysql.connector.connect(
    		host=config('HOST_DB'),
    		user=config('USER_DB'),
    		password=config('PASSWORD_DB'),
    		database=config("DATABASE"),
	)

	cursor = mydb.cursor(buffered=True)
	try:
		request = "SELECT mac, ip, adherent_id FROM routeurs"
		cursor.execute(request)
		mydb.close()
		for j in cursor.fetchall():
			dico = {"mac":j[0], "ip":j[1], "adherent_id":j[2]}
			liste.append(dico)
		return render_template("devices.html", liste=liste)
	except mysql.connector.errors.ProgrammingError:
		mydb.close()
		return "<h1> Une erreur est survenue</h1>"
#mysql.connector.errors.InterfaceError
from asyncio import subprocess
from app import app
from config import db
from flask import render_template, request
from decouple import config
import os.path
import re
import subprocess
from flask_cas import login_required

import os

@app.route("/firmware/<string:device>/<string:mac>_<string:ip>")
@login_required
def firmware_create(device, mac, ip) :
    ### je suppose que je reçois les informations pertinentesrecv_info()
    # je dois envsubst ici, du coup me faut un template de conf envsubst()
    if not mac_validator(mac) :
        return render_template("errors/500.html", error="Format de mac incorrect")
    if not ipv4_validator(ip) :
        return render_template("errors/500.html", error="Format d'IP incorrect")
    if device != "750" and device != "750s":
	    return render_template("errors/404.html", error="Type de routeur inexistant")
    if not os.path.exists(config("PATH_TO_SCRIPT")) :
        return render_template("errors/500.html", error="Impossible de trouver le script de génération")
    subprocess.Popen(['bash', config("PATH_TO_SCRIPT"), mac, ip]) #Popen parce qu'on lance le processus en arrière plan
    return render_template("generate.html", model=device)

@app.route("/firmware/logs/", methods = ['POST'])
@login_required
def firmware_logs() :
    if request.method == 'POST' :
        data = request.get_json()
        return data["message"]

def mac_validator(mac_adress) :
    print(mac_adress)
    if len(mac_adress) != 17 :
        return False
    regex_deuxpoints = re.compile('\d{2}:\d{2}:\d{2}:\d{2}:\d{2}:\d{2}')
    regex_tirets = re.compile('\d{2}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}')

    if regex_deuxpoints.match(mac_adress) is None :
        if regex_tirets.match(mac_adress) is None :
            return False
        else :
            mac_adress = mac_adress.replace("-", ":")
    return True

def ipv4_validator(ip_adress) : #format d'IP attendu, xx.xx.xx.xx
    if len(ip_adress) > 12 :
        return False
    regex_attendu = re.compile('\d{2}.\d{2}.\d{2}.\d{2}')

    if regex_attendu.match(ip_adress) is None :
        return False
    return True

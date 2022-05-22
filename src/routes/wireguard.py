from app import app
from config import db
from flask import render_template
from flask_cas import login_required
import os

@app.route("/wireguard/")
@login_required
def parse_conf() :
    try:
        array, array2 = read_wg()
    except IOError :
        #return "Impossible d'ouvrir le fichier wg0.conf en lecture"
        return render_template("errors/500.html", error="Impossible d'ouvrir le fichier wg0.conf en lecture")
    return render_template("wireguard.html", array=array["Interface"], array2=array2)

def read_wg() :
    '''
    Il faut parser le fichier de conf wireguard 
    '''
    array = {}; array2 = {}
    dico={}
    test=""
    aux=""
    count=0
    try:
        with open('routes/wg0.conf') as f:
            lines = f.read().splitlines()
            for line in lines :
                if line != "" :
                    if line[0] != "#":
                        if "[" in line :
                            aux=line.strip("[]")
                            if "Peer" in line :
                                aux += str(count)
                                count += 1
                            dico={}
                        else :
                            test=''
                            for carac in line :
                                if carac == " " :
                                    break
                                test += carac

                            dico[test] = line[len(test) + 3 :]
                            array[aux] = dico
            array2 = dict(array)
            del array2["Interface"]
            del array["Interface"]["PrivateKey"]
    except IOError :
        raise IOError

    return array, array2

def update_wg() :
    pass

def delete_wg() :
    pass
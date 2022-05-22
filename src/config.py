from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from flask_cas import CAS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cas = CAS()
cas.init_app(app)


app.config['CAS_SERVER'] = config("CAS_SERVER")
app.config['CAS_LOGIN_ROUTE'] = config('CAS_LOGIN_ROUTE')
app.config['CAS_LOGOUT_ROUTE'] = config('CAS_LOGOUT_ROUTE')
app.config['CAS_VALIDATE_ROUTE'] = config('CAS_VALIDATE_ROUTE')
app.config['CAS_AFTER_LOGIN'] = config('CAS_AFTER_LOGIN')
app.config['CAS_AFTER_LOGOUT'] =config('CAS_AFTER_LOGOUT')

app.config['SECRET_KEY'] = config('SECRET_KEY')

#from models.Club import Club
#from models.Association import Association
#from models.Event import Event

from routes import admin, display, devices, openwrt, wireguard

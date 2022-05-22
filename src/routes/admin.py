from app import app
from config import db
from flask import render_template
from flask_cas import login_required

@app.route("/admin/")
@login_required
def admin() :
    return render_template("admin.html")
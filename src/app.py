from config import app
from config import db
from flask_cors import CORS

#db.create_all()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


if __name__== '__main__' :
    db.create_all()
    app.run(debug=True)

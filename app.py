import os
basedir = os.path.abspath(os.path.dirname(__file__)) 
#_file_ temporary name space of file 

#see where secret key is being used (being declared here)
# reference previous file for database url but example : DATABASE_URL="postgresql:///wordcount_dev"
# return data from json via the URL to the html/js pushing from the back end to front end 
from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#pull from database to serve engine, 
@app.route('/')
def home():
    return render_template("index.html") 

if __name__ == '__main__':
    app.run()
    #debug=True for testing purposes 
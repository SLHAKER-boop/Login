from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

db_name = 'Data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)



class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FistName = db.Column(db.String)
    LastName = db.Column(db.String)
    UserName = db.Column(db.String)
    Gmail = db.Column(db.String)
    password = db.Column(db.String)
    
    
    
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/")
@app.route("/login")
def login():
    return render_template("LoginHTML.html")

@app.route("/register")
def register():
    return render_template("RegisterHTML.html")

if __name__ == "__main__":
    app.run(debug=True)
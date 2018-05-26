from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:root@localhost/Filmdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(),unique=True)
    password=db.Column(db.String())

    def __repr__(self):
        return '<User {}>'.format(self.username)


@app.route("/")
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)


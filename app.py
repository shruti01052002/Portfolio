from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
db = SQLAlchemy(app)

@app.route('/')
def base():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)
import sqlite3

from flask import Flask, jsonify, render_template


app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

import sqlite3

from flask import Flask, jsonify, render_template


app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/get-data")
async def get_data():
    return jsonify({"test": 123})

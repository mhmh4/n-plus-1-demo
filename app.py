import sqlite3

from flask import Flask, jsonify, render_template


app = Flask(__name__)

conn = sqlite3.connect("./instance/database.sqlite", check_same_thread=False)


def get_authors():
    cur = conn.cursor()
    sql = "SELECT * FROM Author"
    cur.execute(sql)
    x = cur.fetchall()
    print(x)
    return x


def get_books(author_id):
    cur = conn.cursor()
    sql = f"SELECT * FROM Book WHERE author_id = {author_id}"
    cur.execute(sql)
    x = cur.fetchall()
    print(x)
    return x



@app.get("/")
def index():
    return render_template("index.html")


@app.get("/get-data")
async def get_data():
    authors = get_authors()
    output = []
    for author in authors:
        author_id = author[0]
        books = get_books(author_id)
        output.append(books)
    return jsonify(output)


def query_all():
    cur = conn.cursor()
    sql = f"SELECT * FROM Author, Book JOIN Author ON Book.author_id = Author.id"
    cur.execute(sql)
    x = cur.fetchall()
    print(x)
    return x


@app.get("/get-data-2")
async def get_data2():
    return jsonify(query_all())

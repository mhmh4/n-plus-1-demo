import sqlite3

from flask import Flask, jsonify, render_template

app = Flask(__name__)
conn = sqlite3.connect("./instance/database.sqlite", check_same_thread=False)


def get_authors():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Author")
    res = cur.fetchall()
    cur.close()
    return res


def get_books_1(author_id):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM Book WHERE author_id = {author_id}")
    res = cur.fetchall()
    cur.close()
    return res


def get_books_2():
    cur = conn.cursor()
    sql = f"SELECT * FROM Book JOIN Author ON Book.author_id = Author.id"
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    return res


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/get-data")
async def get_data():
    authors = get_authors()
    output = []
    for author in authors:
        author_id = author[0]
        books = get_books_1(author_id)
        output.append(books)
    return jsonify(output)


@app.get("/get-data-2")
async def get_data2():
    books = get_books_2()
    return jsonify(books)

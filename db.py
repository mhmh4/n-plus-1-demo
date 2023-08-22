import sqlite3
import sys

db = sqlite3.connect("./instance/database.sqlite")
if not db:
    sys.exit()

with open("schema.sql", encoding="utf-8") as f:
    db.executescript(f.read())

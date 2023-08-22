import random
import sqlite3
import sys

DATABASE_PATH = "./instance/database.sqlite"

conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
if not conn:
    sys.exit()

TABLES_SCHEMA = """
CREATE TABLE Author (
  id INTEGER PRIMARY KEY
);

CREATE TABLE Book (
  id INTEGER PRIMARY KEY,
  author_id INTEGER,
  FOREIGN KEY (author_id) REFERENCES Author(id)
);
"""

with open("schema.sql", encoding="utf-8") as f:
    conn.executescript(TABLES_SCHEMA)


NUM_AUTHORS = 10_000

cur = conn.cursor()

for i in range(1, NUM_AUTHORS + 1):
    cur.execute(f"INSERT INTO Author (id) VALUES ({i})")
    for _ in range(random.randint(1, 5)):
        cur.execute(f"INSERT INTO Book (author_id) VALUES ({i})")

conn.commit()
cur.close()

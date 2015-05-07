import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

table_movies = """
CREATE TABLE IF NOT EXISTS 
Movies(id INTEGER PRIMARY KEY, name TEXT, rating NUMERIC)
"""

table_projection = """
CREATE TABLE IF NOT EXISTS
Projections(id INTEGER PRIMARY KEY, 
movie_id INTEGER,
type TEXT,
date DATE,
time TIME,
FOREIGN KEY(movie_id) REFERENCES Movies(id)
)
"""

table_reservations = """
CREATE TABLE IF NOT EXISTS
Reservations(id INTEGER PRIMARY KEY,
username TEXT,
projection_id INTEGER,
row INTEGER,
col INTEGER,
FOREIGN KEY(projection_id) REFERENCES Projections(id)
)
"""

all_creations = [table_movies, table_projection, table_reservations]

for each in all_creations:
    cursor.execute(each)

connection.commit()

 
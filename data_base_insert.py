import sqlite3
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

INSERT_MOVIE1 = """
INSERT INTO Movies(name, rating)
VALUES ("The Hunger Games: Catching Fire", 7.9)
"""
cursor.execute(INSERT_MOVIE1)

INSERT_MOVIE2 = """
INSERT INTO Movies(name, rating)
VALUES ("Wreck-It Ralph", 7.8)
"""
cursor.execute(INSERT_MOVIE2)

INSERT_MOVIE3 = """
INSERT INTO Movies(name, rating)
VALUES ("Her", 8.3)
"""
cursor.execute(INSERT_MOVIE3)

INSERT_PROJECTION1 = """
INSERT INTO Projections(movie_id,type,date,time)
VALUES (1,"3D", "2014-04-01", "19:10")
"""
cursor.execute(INSERT_PROJECTION1)

INSERT_PROJECTION2 = """
INSERT INTO Projections(movie_id,type,date,time)
VALUES (1,"2D", "2014-04-01", "19:00")
"""
cursor.execute(INSERT_PROJECTION2)

INSERT_PROJECTION3 = """
INSERT INTO Projections(movie_id,type,date,time)
VALUES (1,"4DX", "2014-04-02", "21:00")
"""
cursor.execute(INSERT_PROJECTION3)

INSERT_PROJECTION4 = """
INSERT INTO Projections(movie_id,type,date,time)
VALUES (3,"2D", "2014-04-05", "20:20")
"""
cursor.execute(INSERT_PROJECTION4)

INSERT_PROJECTION5 = """
INSERT INTO Projections(movie_id,type,date,time)
VALUES (2,"3D", "2014-04-02", "22:00")
"""
cursor.execute(INSERT_PROJECTION5)

INSERT_PROJECTION6 = """
INSERT INTO Projections(movie_id,type,date,time)
VALUES (2,"2D", "2014-04-02", "19:30")
"""
cursor.execute(INSERT_PROJECTION6)

INSERT_RESERVATION1 = """
INSERT INTO Reservations(username, projection_id, row, col)
VALUES ("RadoRado",1, 2, 1)
"""
cursor.execute(INSERT_RESERVATION1)

INSERT_RESERVATION2 = """
INSERT INTO Reservations(username, projection_id, row, col)
VALUES ("RadoRado",1, 3, 5)
"""
cursor.execute(INSERT_RESERVATION2)

INSERT_RESERVATION3 = """
INSERT INTO Reservations(username, projection_id,row, col)
VALUES ("RadoRado",1, 7, 8)
"""
cursor.execute(INSERT_RESERVATION3)

INSERT_RESERVATION4 = """
INSERT INTO Reservations(username, projection_id,row, col)
VALUES ("Ivo",3, 2, 1)
"""
cursor.execute(INSERT_RESERVATION4)

INSERT_RESERVATION5 = """
INSERT INTO Reservations(username, projection_id,row, col)
VALUES ("Ivo",3, 1, 1)
"""
cursor.execute(INSERT_RESERVATION5)

INSERT_RESERVATION6 = """
INSERT INTO Reservations(username, projection_id,row, col)
VALUES ("Mysterious",5, 2, 3)
"""
cursor.execute(INSERT_RESERVATION6)

INSERT_RESERVATION7 = """
INSERT INTO Reservations(username, projection_id,row, col)
VALUES ("Mysterious",5, 2, 4)
"""
cursor.execute(INSERT_RESERVATION7)

connection.commit()

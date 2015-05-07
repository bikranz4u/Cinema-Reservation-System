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

INSERT_PROJESTION1 = """
INSERT INTO Projestions(type,data,time)
VALUES ("3D", 2014-04-01, 19:10)
"""
cursor.execute(INSERT_PROJESTION1)

INSERT_PROJESTION2 = """
INSERT INTO Projestions(type,data,time)
VALUES ("2D", 2014-04-01, 19:00)
"""
cursor.execute(INSERT_PROJESTION2)

INSERT_PROJESTION3 = """
INSERT INTO Projestions(type,data,time)
VALUES ("4DX", 2014-04-02, 21:00)
"""
cursor.execute(INSERT_PROJESTION3)

INSERT_PROJESTION4 = """
INSERT INTO Projestions(type,data,time)
VALUES ("2D", 2014-04-05, 20:20)
"""
cursor.execute(INSERT_PROJESTION4)

INSERT_PROJESTION5 = """
INSERT INTO Projestions(type,data,time)
VALUES ("3D", 2014-04-02, 22:00)
"""
cursor.execute(INSERT_PROJESTION5)

INSERT_PROJESTION6 = """
INSERT INTO Projestions(type,data,time)
VALUES ("2D", 2014-04-02, 19:30)
"""
cursor.execute(INSERT_PROJESTION6)

INSERT_RESERVATION1 = """
INSERT INTO Reservations(username, row, col)
VALUES ("RadoRado", 2, 1)
"""
cursor.execute(INSERT_RESERVATION1)

INSERT_RESERVATION2 = """
INSERT INTO Reservations(username, row, col)
VALUES ("RadoRado", 3, 5)
"""
cursor.execute(INSERT_RESERVATION2)

INSERT_RESERVATION3 = """
INSERT INTO Reservations(username, row, col)
VALUES ("RadoRado", 7, 8)
"""
cursor.execute(INSERT_RESERVATION3)

INSERT_RESERVATION4 = """
INSERT INTO Reservations(username, row, col)
VALUES ("Ivo", 2, 1)
"""
cursor.execute(INSERT_RESERVATION4)

INSERT_RESERVATION5 = """
INSERT INTO Reservations(username, row, col)
VALUES ("Ivo", 1, 1)
"""
cursor.execute(INSERT_RESERVATION5)

INSERT_RESERVATION6 = """
INSERT INTO Reservations(username, row, col)
VALUES "Mysterious", 2, 3)
"""
cursor.execute(INSERT_RESERVATION6)

INSERT_RESERVATION7 = """
INSERT INTO Reservations(username, row, col)
VALUES "Mysterious", 2, 4)
"""
cursor.execute(INSERT_RESERVATION7)

connection.commit()

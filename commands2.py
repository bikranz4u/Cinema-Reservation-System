import sqlite3
from matrix import Matrix
import re
db = sqlite3.connect("database.db")
cursor = db.cursor()


class Commands:

    def __init__(self):
        self.__show_movies = """
        SELECT name,rating
        FROM movies
        ORDER BY rating 
    """
        self.__only_id = """
        SELECT id, date, time,type
        FROM projections
        WHERE movie_id=(?)
        """
        self.__id_date = """
        SELECT id, time, type
        FROM projections
        WHERE movie_id=(?)
        AND date=(?)
        """

    def show_movies(self, cursor_arg = None):
        result = cursor.execute(self.__show_movies)
        for movie in result:
            print(movie)

    def show_movies_projections(self, movie_id, date = None):
        if date == None:
            result = cursor.execute(self.__only_id, (movie_id,))
            for movie in result:
                print(movie)

        else:
            result = cursor.execute(self.__id_date, (movie_id, date))
            for movie in result:
                print(movie)


    def choose_seat(self):
        seat = input("Choose seat ")
        row = int(seat[1])
        col = int(seat[3])
        Matrix.check_borders(row, col)





    def make_reservation(self):
        name = input("Choose name> ")
        number_tickets = int(input("Choose numbers of tickets> "))
        print("Current movies: ")
        self.show_movies()

        id = int(input("Choose a movie> "))
        self.show_movies_projections(id)

        projection = int(input("Choose a projection> "))
        print("Available seats(marked with a dot): ")
        Matrix.print_matrix()
        self.choose_seat()






def main():
    c = Commands()
    # c.show_movies()
    #c.show_movies_projections(1, "2014-04-01")
    c.make_reservation()

if __name__ == '__main__':
    main()

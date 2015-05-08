import sqlite3
from matrix import Matrix
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

    def check_number_of_tickets(self):
        pass


    def choose_seat(self):
        seat = input("Choose seat ")
        row = int(seat[1])
        col = int(seat[3])
        Matrix.check_borders(row, col)

    def make_reservation(self):
        name = input("Choose name> ")
        number_tickets = int(input("Choose numbers of tickets> "))
        Matrix.get_free_seats(number_tickets)
        if Matrix.get_free_seats(number_tickets) == True:
            print("Current movies: ")
            self.show_movies()

            id = int(input("Choose a movie> "))
            self.show_movies_projections(id)

            projection = int(input("Choose a projection> "))
            print("Available seats(marked with a dot): ")
            Matrix.print_matrix()
            counter = 0
            while counter < number_tickets:
                if self.choose_seat():
                    counter +=1

        else:
            self.exit()

    def exit(self):
        pass


def main():
    c = Commands()


if __name__ == '__main__':
    main()

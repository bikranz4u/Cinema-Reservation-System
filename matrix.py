matrix = [
[" ",1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
[1, ".",".",".",".",".",".",".",".",".","."],
[2, ".",".","X","X",".",".",".",".",".","."],
[3, ".",".",".",".",".",".",".",".",".","."],
[4, ".",".",".",".",".",".",".",".",".","."],
[5, ".",".",".",".",".",".",".",".",".","."],
[6, ".",".",".",".",".",".",".",".",".","."],
[7, ".",".",".",".",".",".",".",".",".","."],
[8, ".",".",".",".",".",".",".",".",".","."],
[9, ".",".",".",".",".",".",".",".",".","."],
[10, ".",".",".",".",".",".",".",".",".","."],
]

class Matrix:



    @staticmethod
    def print_matrix():
        n = len(matrix)
        m = len(matrix[0])

        for i in range(0, n):
            print()
            for j in range(0, m):
                print(matrix[i][j], end="")

    @staticmethod
    def  check_borders(col, row):
        if col > len(matrix) or row > len(matrix[0]):
            print("Lol ... No!")
            return False
        elif matrix[col][row] == 'X':
            print("This is already taken")
            return False
        else:
            print("This is your reservation")
            return True

    @staticmethod
    def get_free_seats(number_tickets):
        count = 0
        n = len(matrix)
        m = len(matrix[0])
        for i in range (0,n):
            for j in range (0,m):
                if matrix[i][j] == ".":
                    count += 1

        return number_tickets <= count



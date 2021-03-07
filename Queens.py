import sys

class Queens (object):
    def __init__ (self,n):
        self.board = []
        self.n = n
        self.count = 0
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

      # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                self.board[i][j], end = ' '


# check if a position on the board is valid
    def is_valid(self, row, col):
        for i in range (self.n):
            if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
                return False
        for i in range (self.n):
            for j in range (self.n):
                row_diff = abs (row - i)
                col_diff = abs (col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

# do the recursive backtracking
    def recursive_solve(self, col):
        if (col == self.n):
            self.count += 1
        else:
            for i in range(self.n):
                if self.is_valid(i, col):
                    self.board[i][col] = 'Q'
                    # removed if statement because
                    self.recursive_solve(col + 1)
                    self.board[i][col] = '*'


# if the problem has a solution print the board
    def solve(self):
        count = 0
        # changed this to count solutions, not just print one solution
        self.recursive_solve(0)
        print(self.count)

def main():
    # read the size of the board
    line = sys.stdin.readline()
    line = line.strip()
    n = int (line)
    # create a chess board
    queens = Queens(n)

    # place the queens on the board
    queens.solve()

main()

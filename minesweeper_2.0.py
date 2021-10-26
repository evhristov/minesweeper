from random import randint


class Grid():

    def __init__(self,size: int, mines: int):
        self.size = size
        self.mines = mines
        self.hidden_grid = [[0]*size for _ in range(size)]
        self.player_grid = []

    def generate_mines(self):

        for _ in range(self.mines):
            while True:
                x = randint(0, self.size - 1)
                y = randint(0, self.size - 1)
                if self.hidden_grid[x][y] != "*":
                    break

            self.hidden_grid[x][y] = "*"

            for i in range(-1, 2):
                if 0 <= x + i <= self.size - 1:
                    for j in range(-1, 2):
                        if 0 <= y + j <= self.size - 1:
                            if not self.hidden_grid[x + i][y + j] == "*":
                                self.hidden_grid[x + i][y + j] += 1

    def __repr__(self):

        result = ""
        for _ in self.hidden_grid:
            _ = [str(x) for x in _]
            result += " ".join(_) + "\n"
        return result



def main():
    x = Grid(10,5)
    print(str(x))
    x.generate_mines()
    print(str(x))
main()
import numpy as np


class Board:
    def __init__(self, dim: int = 4, colors: int = 4):
        self.dim = dim
        self.ncolors = colors
        self.board = np.random.randint(1, self.ncolors, (self.dim, self.dim))

    def draw(self):

        for line in range(self.dim):
            for column in range(self.dim):
                print(f"{self.board[line][column]} | ", end="")
            print(" ")
            print("-"*4*self.dim)

    def update(self, color: int = 0):
        prev_color = self.board[0][0]
        if(color >= 0 and color < self.ncolors):
            self.flood(prev_color, color, (0, 0))

    def __isvalidpos(self, pos: tuple):
        return pos[0] >= 0 and pos[0] < self.dim and pos[1] >= 0 and pos[1] < self.dim

    def flood(self, prev_color: int = 0, new_color: int = 0, pos: tuple = (0, 0)):
        if(self.__isvalidpos(pos) and self.board[pos[0], pos[1]] == prev_color):
            self.board[pos[0], pos[1]] = new_color
            self.flood(prev_color, new_color, (pos[0], pos[1]+1))
            self.flood(prev_color, new_color, (pos[0]+1, pos[1]))


class Game:

    def __init__(self, configuration: dict = {}):
        self.command = "start"
        dim = configuration['board']['dim']
        colors = configuration['board']['colors']
        self.board = Board(dim=dim, colors=colors)

    def menu(self):
        print(" flood-it ".center(20, "="))

    def draw(self):
        self.board.draw()

    def __game_loop(self):
        while(self.command != "stop"):
            self.menu()
            self.draw()
            self.command = input('Insira um comando: ')
            self.update()

    def update(self):
        color = int(self.command)
        print(color)
        self.board.update(color)

    def main(self):
        self.__game_loop()


config = {'board': {'colors': 6, 'dim': 8}}
game = Game(configuration=config)
game.main()

import numpy as np

class Board:
  def __init__(self, dim:int=4, colors:int=4):
    self.dim = dim
    self.ncolors = colors
    self.board = np.random.randint(1, self.ncolors, (self.dim, self.dim))

  def draw(self):

    for line in range(self.dim):
      for column in range(self.dim):
        print(f"{self.board[line][column]} | ", end="")
      print(" ")
      print("-"*16)

class Game:

  def __init__(self):
    self.command = "start"
    self.board = Board()

  def menu(self):
    print(" flood-it ".center(20, "="))

  def draw(self):
    self.board.draw()

  def __game_loop(self):
    while(self.command != "stop"):
      self.menu()
      self.draw()
      self.command = input('Insira um comando: ')

  def main(self):
    self.__game_loop()


game = Game()
game.main()
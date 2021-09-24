import random


def dice():
  dice = random.randint(0,7)
  return dice
def choose_type():
    rand = random.randint(1,10)
    if rand <= 2:
      return '+'
    elif rand <= 4:
      return '-'
    else:
      return 'o'
class Cell:
  def __init__(self, position):
    self.position = position
    self.cell_type = choose_type()
    if self.cell_type == '+' and self.position != 99:
      self.next_cell = random.randint(self.position + 1, 99)
    elif self.cell_type == '-' and self.position != 1:
      self.next_cell = random.randint(1, self.position - 1)
    else:
      self.next_cell = self.position
    def __str__(self):
      return f'{self.cell_type}:{self.next_cell}'
class Board:
  def __init__(self):
    self.size = 10
    self.cells = []

    for i in range(1,100):
      c = Cell(i)
      self.cells.append(c)

  def show(self):
    counter = 1
    for i in range(self.size):
      for j in range(self.size):
        print(self.cells[counter], end='\t')
        counter += 1
      print('\n')



class Player:
  def __init__(self, cells, name):
    self.name = name
    self.cells = cells
    self.lst = [0]
    while True:
      self.move = dice()
      if self.lst[-1] < 99:
        self.lst.append(self.cells[self.lst[-1] + self.move])
      elif self.lst[-1] > 99:
        self.lst.pop()
      elif self.lst[-1] == 99:
        print(f'{self.name} is winner')
        break
      print(self.lst[-1], end=' ')

sina = Cell(2)
sina = Board().cells
print(sina)
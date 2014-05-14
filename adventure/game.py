#external modules
from time import sleep

#internal modules
from data import GameData

#game constants
TICK = 0.1  #number of seconds to delay between game loops
SCREENWIPE = 200 #number of blank lines for a screen wipe

def play():
  game = Game()
  while (game.playing):
    sleep(TICK)
    game.update()

class Game(object):
  def __init__(self):
    self.playing = True
    self.loadGame()
    self.screenWipe()
    self.displayTitle()

  def loadGame(self):
    self.data = GameData('adventure/game.dat')

  def screenWipe(self):
    for _ in range(SCREENWIPE):
      print ""

  def displayTitle(self):
    self.playerName = raw_input(self.data.title+'>> ')
    print "Nice try, "+self.playerName
    self.playing = False

  def update(self):
    self.playing = False

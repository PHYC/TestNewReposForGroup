#external modules
from time import sleep
from random import shuffle

#internal modules
from data import GameData
from parser import enshorten

from constants import TICK,SCREENWIPE
directions=['north','east','south','west']
confusions=['Come again?','Say what now?','Huh?','Whuttawut?','Try again.','Use your WORDS.',"Not followin' ya..."]
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
    self.switchRoom(1000)

  def switchRoom(self,num):
    self.playerRoom = num
    self.displayRoom()

  def displayRoom(self):
    self.screenWipe()
    self.getRoom().display()

  def getRoom(self):
    return self.data.rooms[self.playerRoom]

  def update(self):
    self.interpretAction(raw_input('>> '+self.playerName+'$ '))

  def interpretAction(self,line):
    if len(line) == 0:
      command = 'foo'
    else:
      command = line.split()[0].lower()
      if len(line.split()) > 1:
        args = line.split()[1].lower()
      else:
        args = ''
    if command == 'quit':
      self.playing = False
    elif command == 'look':
      self.displayRoom()
    elif command == 'ls':
      self.displayRoom()
      print enshorten('An ethereal voice speaks, "Okay, I got what you meant, but next time use the \'look\' command. Jackass."')
    elif command == 'enter':
      if args in self.getRoom().doors:
        self.switchRoom(self.getRoom().doors[args])
      elif args == 'sandman':
        print "Yes, very clever.\n"
      else:
        print "You'll have to specify a valid exit...\n"
    elif command == 'help':
      print "Available commands:\n"+enshorten("quit look enter north east south west dance")
    elif command in directions:
      if command in self.getRoom().exits:
        self.switchRoom(self.getRoom().exits[command])
      else:
        print enshorten("Oof! That way is obstructed!")
    elif command in self.getRoom().exits:
      self.switchRoom(self.getRoom().exits[command])
    elif command == 'dance':
      print enshorten("You dance the dance of your people. You feel more alive than ever before!")
    else:
      shuffle(confusions)
      print confusions[0]+" (try 'help' for a list of commands)\n"
      self.update()

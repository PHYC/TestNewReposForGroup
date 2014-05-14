#from items import Item
#from mobs import Mob
from rooms import Room

class GameData(object):
  def __init__(self,fileName):
    self.items=[]
    self.mobs=[]
    self.rooms={}
    file=open(fileName).readlines()
    while (len(file) > 0):
      type = file.pop(0)[1:-1]
      if type == 'Title':
        self.title = self.readTitle(file)
      if type == 'Item':
        #self.addItem(file)
        print 'Item found'
      if type == 'Mob':
        #self.addMob(file)
        print 'Mob found'
      if type == 'Room':
        self.addRoom(Room(file))

  def readTitle(self,file):
    output = ''
    line = file.pop(0)
    while (line[0] != '~'):
      output+=line
      line = file.pop(0)
    return output

  def addRoom(self,room):
    if room.id in self.rooms:
      print "-------------------------------------------------------------"
      print "WARNING: DUPLICATE ROOM IDS FOUND. YA DONE FUCKED UP, A-ARON."
      print "----room id: "+str(room.id)+" --- room name: "+room.name+" ----"
      raise
    else:
      self.rooms[room.id]=room

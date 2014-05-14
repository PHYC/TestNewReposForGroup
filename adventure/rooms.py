from parser import parse

class Room(object):
  def __init__(self,data):
    self.funcs={'id':self.setID,
                'name':self.setName,
                'description':self.setDescription,
                'doors':self.setDoors,
                'exits':self.setExits,
                'items':self.setItems,
                'mobs':self.setMobs}
    self.loadDefaults()
    self.readData(data)
    print "Read new room, ID: "+str(self.id)

  def loadDefaults(self):
    self.id=0
    self.name='The void'
    self.description='You float in black space.'
    self.doors={}
    self.exits={}
    self.items=[]
    self.mobs=[]

  def readData(self,data):
    line=data.pop(0)
    while (line[0] != '~'):
      vals=parse(line)
      if vals[0] in self.funcs:
        self.funcs[vals[0]](vals[1])
      else:
        print "------------------------------------------"
        print "WARNING: ROOM CONTAINS UNMAPPABLE PROPERTY"
        print "---- room id: "+str(self.id)+" --- property: "+vals[0]+" ----"
        raise
      line=data.pop(0)

  def setID(self,id):
    self.id = int(id)

  def setName(self,name):
    self.name = name

  def setDescription(self,desc):
    self.description=desc

  def setDoors(self,doors):
    for d in doors.split():
      pair=d.split('-')
      self.doors[pair[0]]=int(pair[1])

  def setExits(self,exits):
    for e in exits.split():
      pair=e.split('-')
      self.exits[pair[0]]=int(pair[1])

  def setItems(self,items):
    self.items=map(int,items.split())

  def setMobs(self,mobs):
    self.mobs=map(int,mobs.split())



class Player:
  name = "Hector"
  hp = 10
  location = 0
  mp = 5

  def __init__(self):
    self.name = input("What is your hero's name?\n")

  def getName(self):
    return self.name

  def getHealth(self):
    return self.hp  
  
  def getLocation(self):
    return self.location

  def setLocation(self, loc):
    self.location = loc 

    
    
class Room:
  roomNum = 0
  desc = "This is a room with some description"
  exits = {}
  mobs = {}

  def __init__(self, num, description, ex, mobs):
    self.desc = description
    self.exits = ex
    self.mobs = mobs
    self.roomNum = num

 
  
  def displayRoom(self):
    print(self.desc)
    output = "Exits: "
    for i in self.exits:
      output += i + " "
    print(output)
    
    def getRoomNum(self):
      return self.roomNum
    def getDesc(self):
      return self.desc
    def getExits(self):
      return self.exits
    def getMobs(self):
      return self.mobs    
        
    def setRoomNum(self, value):
      self.roomNum = value
    def setDesc(self, value):
      self.desc = value
    def setExits(self, key, value): 
      self.exits[key]= value    
    def setMob(self, key, value):
      self.mobs[key] = value

      
def createWorld(roomList):
  testRoom = Room(0, "This is the starting room", {"e": 1, "s": 4 }, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(1, "This is room 1", {"w": 0, "s": 5 ,"e": 2}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(2, "This is room 2", {"e": 3, "s": 6,"w": 1}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(3, "This is room 3", {"s": 7 ,"w": 2}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(4, "This is room 4", {"n": 0, "s": 8 ,"e": 5}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(5, "This is room 5", {"n": 1, "s": 9 ,"w": 4, "e": 6}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(6, "This is room 6", {"n": 2, "s": 10 ,"w": 5, "e": 7}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(7, "This is room 7", {"n": 3, "s": 11 ,"w": 6}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(8, "This is room 8", {"n": 4, "s": 12 ,"e": 9}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(9, "This is room 9", {"n": 5, "s": 13 ,"w": 8,"e": 10}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(10, "This is room 10", {"n": 6, "s": 14 ,"w": 9,"e": 11}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(11, "This is room 11", {"n": 7, "s": 15 ,"w": 10}, {"goblin": 7 })
  roomList.append(testRoom) 
  testRoom = Room(12, "This is room 12", {"n": 8, "e": 13}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(13, "This is room 13", {"n": 9, "e": 14 ,"w": 12}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(14, "This is room 14", {"n": 10, "e": 15 ,"w": 13}, {"goblin": 7 })
  roomList.append(testRoom)
  testRoom = Room(15, "This is room 15", {"n": 11, "w": 14}, {"goblin": 7 })
  roomList.append(testRoom)
  
  return roomList

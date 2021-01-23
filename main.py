from game_classes import *
import sys, os


running = True
player = None
roomList = []
# Need to expand logic on this
def combat(enemy):
    print(f"You are attacking {enemy}")

# Need to expand logic
# Verify object is in Room and return desc\info 
def look(obj):
  print(f"You closely examine {obj}")


def parseResp(response):
  response = response.lower()
  if response in "e s w n":
    choosePath(response)
  if "kill" in response:
    response = response.split()
    combat(response[1])
  if "look" in response:
    response = response.split()
    look(response[1])

def choosePath(path):
  global player
  global running
  room_obj = roomList[player.location]
  print(room_obj.exits)
  moved = False
  while moved == False:
    if path in room_obj.exits:
      loc = room_obj.exits[path]
      player.setLocation(loc)
      roomList[loc].displayRoom()
      moved = True
    else:
      path = input("That is not a valid direction\n").lower()
      if path[0] == 'q':
        print("You have quit the game")
        running = False
        break


# 0  1  2  3
# 4  5  6  7
# 8  9  10 11
# 12 13 14 15


def quit():
    print("Quitting game\n")
    sys.exit(0)

def help():
    print(
    '''
    - Use n,s,e,w to navigate through the map
    - Available exits will be shown for each room you are in
    - You can use "q" to quit the game at any time
    - More instruction to come as game expands    
    '''
    )
    input("Press any key to continue")
    titleScreen()

def titleScreen():
    global running
    print('''
  *********************************************
  #############################################
  #*#                                       #*#
  #*#                                       #*#
  #*#              WELCOME                  #*#
  #*#                TO                     #*#
  #*#             TEST GAME                 #*#
  #*#            ____________               #*#
  #*#                                       #*#
  #*#                                       #*#
  #*#           1. Begin                    #*#
  #*#           2. How to Play              #*#
  #*#           3. Quit                     #*#
  #*#                                       #*#
  #*#                                       #*#
  #*#                                       #*#
  |||||||||||||||||||||||||||||||||||||||||||||
  ''')


  
    while True:
        choice = int(input("Make a selection\n"))
        if choice == 1:
            buildGame()
            play()
        elif choice == 2:
            help()
        elif choice == 3:
            quit()
        else:
            print("Make a valid selection\n")

def buildGame():
  global roomList
  global player
  roomList = createWorld(roomList)
  player = Player()
  print("Welcome " + player.getName())

def play():
  global running
  roomList[player.location].displayRoom()
  while running:
    response = input(">>>")
    if response == "quit" or response == "q":
      quit()
    elif response == "loc":
      print(player.location)  
    else:
    
      parseResp(response)  

titleScreen()



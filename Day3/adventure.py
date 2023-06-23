##AUTHOR: Raagavee Selvamohan
#Day 3 Create an adventure game
#Using user input to pick between different options to get to the end.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Get Users first input
choice1 = input("You have come to a crossroad\nWhere do you want to go?\nType 'left' or 'right'\n").lower()

#if and else statment to determine the next steps
#if left 
if(choice1 == "left"):
  choice2 = input("You have come to a lake!\nThere is an island in the middle of the lake\nDo you want to wait for a boat or swim to the island?\nType 'wait' or 'swim'\n").lower()
  
  #if wait
  if(choice2 == "wait"):
    choice3 = input("You arrive at the island unharmed\nThere is a house with 3 doors\nWhich door do you pick?\nred, yellow or blue?\n").lower()
    
    #If yellow
    if(choice3 == "yellow"):
      print("You open the door to a portal home!\nYou Win!")
      
    #If red
    elif(choice3 == "red"):
      print("You open the door to a room full of locus!\nGame Over!")
      
    #If blue
    elif(choice3 == "blue"):
      print("You open the doors to human eating beasts!\nGame Over!")
      
    #If user inputs an option not stated in question 
    else:
      print("A door of that colour does not exist!\nGame Over!")
  
  #if Swim    
  else:
    print("You got attacked by a lake monster!\nGame Over!")
    
#If Right    
else:
  print("You fell into a hole!\nGame Over!")
#AUTHOR: Raagavee Selvamohan
#Day 4 Create a rock papers scissors game
#The user inputs a character they want to play then the computer randomly selects a character to play
#then the winner is determined based on what is picked.

#Images
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#impoirt random module so we can perform randomisation
import random

#Put images into list
image = [rock, paper, scissors]

print("Welcome to Rock, Papers, Scissors!")

#get user input and print that image
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
#if user selects correctly from options
if (user >=0 and user <=2):
  print(image[user])

  #get computer input and print that image
  print("Computer chose:")
  comp = random.randint(0,2)
  print(image[comp])

  #User Win Scenarios
  if((user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1)):
    print("You Win!")

  #User Lose Scenarios
  elif((user == 2 and comp == 0) or (user == 0 and comp == 1) or (user == 1 and comp == 2)):
    print("You Lose!")

  #User and Comp Draw Scenarios
  elif user == comp:
    print("You Draw!")
  
  #print incase of errors
  else:
    print("ERROR!")

#if user does not pick correctly from the options
else:
  print("ERROR! You did not type 0, 1 or 2!")
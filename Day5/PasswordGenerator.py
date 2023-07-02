#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

#Order not randomised:
for letter in range(1, nr_letters + 1):
    random_num1 = random.randint(0, len(letters)-1)
    password.append(letters[random_num1])

for symbol in range(1, nr_symbols + 1):
    random_num2 = random.randint(0, len(symbols)-1)
    password.append(symbols[random_num2])

for number in range(1, nr_numbers + 1):
    random_num3 = random.randint(0, len(numbers)-1)
    password.append(numbers[random_num3])

#str_pwd = ""
#for pwd in password:
  #str_pwd += pwd

#print(str_pwd)

#Randomise Order
for change in range (1, len(password)+1):
  random_num4 = random.randint(0, len(password)-1)
  random_num5 = random.randint(0, len(password)-1)

  temp = password[random_num4]
  password[random_num4] = password[random_num5]
  password[random_num5] = temp

str_pwd = ""
for pwd in password:
  str_pwd += pwd

print(str_pwd)
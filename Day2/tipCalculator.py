##AUTHOR: Raagavee Selvamohan
#Day 2 Create a tip caluclator using the users total bill,
#the % they want to tip and the total no. of poeple to split the bill with

#Welcome message
print("Welcome to the tip calculator!")

#Get total bill from user
total_bill = float(input("What is the total bill? £"))

#Get the tip % from user
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

#Get the no,. of people to split bill with from user
no_of_ppl = int(input("How many people to split bill with? "))

#Calucation to split bill by no. of people, and add the tip 
split_Val = (total_bill/no_of_ppl)*(1 + percentage/100)

#format the value to 2 decimal places (Stores as String)
split_Val = "{:.2f}".format(split_Val)

#Print the split bill value
print(f"Each person should pay: £{split_Val}")
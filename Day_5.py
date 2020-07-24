# 1) What are the two primary number types in python?

#integer, float and complex

#2) I want to create a variable x that stores a positive whole number. What type should the variable x be?
#integer

#3) Create a variable called pi that stores the value of 3.14. Then, create anoher variable called radius and
#store an arbitrary value in it. Print the result of pi times radius squared.

pi = 3.14
radius = 5

print( pi * radius ** 2)

#4) Create a variable called 'name' that stores your first name, and create a variable called 'surname' which
#stores your last name. Answer the following:

name = 'Josh'
surname = 'Bartels'

#i) What data type is this? String
#ii) Concatenate the variables together, make sure there's a space between your first and last name. ptiny(name + surname)
#iii) Display the result of your first name lowercase concatenated with your last name uppercase. Example, 'Al CAPONE'

print(name.lower() + surname.upper())


#Control flow
#-------------

# 5) Create a variable called question which prompts the user for the following input:

question = input('Is basic training difficult? ')

#Write an if/else statement that checks to see if the user input is equal to 'y'. If it is
#print a funny message, and if it's equal to 'n' then print another funny message.

question = input("Is basic training difficult? ")



if question == 'y':
    print('Why so serious? ')
elif question == 'n':
    print('good! ')
else:
    print('another funny message')

exit()


# 6) Write an if/elif/else statement for the following case:

#You have a variable called 'budget' which stores the amount of
#money the user have for this month's food budget. Prompt the user to enter
#in their numerical input. First, make sure that they're entering a valid amount.
#The contraints on the system are the following:

#   i) User must enter in a budget that's greater than $0. If it does print an error message
#   ii) User budget cannot exceed $1000. If it does print an error message.
#   iii) If user budget is greater than $550, print "you will eat well this month!"
#   iv)  If user budget is equal to $550 print "this is the average American food budget"
#   v)   If user budget is less than $550, print "this is less than the average American food budget"

budget = int(input('Enter your budget greater that $0: '))


if budget <= 0:
    print('error')
elif budget > 1000:
   print('error budget too high')
elif budget > 550:
    print('you will eat well this month!')
elif budget == 550:
    print('This is the average American food budget')
elif budget < 550:
    print('this is less than the average American food budget')



#Loops and data structures
#-------------------------

#7) Generate the range of even numbers within 1-100 with a while loop. Hint, what operator to use?

start, end = 0, 100

for num in range (start, end + 1):
	if num % 2 == 0:
	 print(num, end=' ')

#8) Create an empty list called nums. Write a for loop that stores 100 random numbers in nums.
#   Hint, generate 100 random numbers:

import random
nums = []
for i in range(1, 101):
    n = random.randint(1, 100)
    nums.append(n)
print(nums)
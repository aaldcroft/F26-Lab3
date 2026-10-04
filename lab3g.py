# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Abby Aldcroft
# Date:Oct 1 2026
# Purpose: 
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file
'''
Write a program that reads values from standard input from user(using input function), stores the inputted values in a list, multiplies each element by 10, and prints the result in reverse order. 

- Create an empty list
- Create a while loop that ends when your list size reaches 6
- Add numbers to your list using input
- Multiply the numbers by 10
- Print out the list in reverse order
'''
#empty list
numList = []

#while loop 
while len(numList) <= 6: # while there are less than or = to 6 numbers the following happens; 
    num = int(input("please enter a number: ")) #user is prompted for a number
    num=num*10 #the number is multiplied by 10
    numList.append(num) # that number is added to end of list

#print out the list
print(numList) 

#print it in reverse order
print(numList[::-1])
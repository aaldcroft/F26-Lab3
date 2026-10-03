# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Abby Aldcroft
# Date: oct 1
# Purpose: Practice adding and removing elements in list.
# Usage: ./lab3d.py

# Follow the specific instructions given in the README.md file
### lab3d.py
### Using list methods to add and remove elements from a list 
'''
- Fill in the required fields in the comment section.
- Create a variable `mylist` that conatins  first 6 natural numbers.
- Use the `append()` method and add a new element, number 7 in the variable `mylis`t. 
- Use the `inser()` method and insert the element 0 at index 0.
- Use the `pop()' method to remove the element from index 2.
- Print the variable `mylist`.
- Add another statement in the script to find the index of the element 6 and
 print `The element 6 is present at the index ---`
'''

mylist = [ 1,2,3,4,5,6 ] 

#append adds to the end of your list
mylist.append(7)

print(mylist)
#insert (how many,value)
mylist.insert(0,0)

print(mylist)

#pop will remove what ever element exists at the value of the index you pleaced, here it took out the 8
mylist.pop(2)

print(mylist)

index6 = mylist.index(6)

print (f" The element 6 is present at the index of" ,index6)



# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Abby Aldcroft 
# Date:Oct 1
# Purpose:
# Usage: ./lab3e.py

# Follow the specific instructions given in the README.md file

'''
## lab3e.py
### Modifying a list and using the list in a loop
- Fill in the required fields in the comment section.
- Create a list variable called `students`. Add the following names in this list: Ama, Elina, Maija, Daniel, Ibrahim.
- Next change the element at index 1 and update this element with "Maggy".
- Now use a` for loop` and iterate over this list and print each element on a separate line. 
'''

#create a list
students = [ 'Ama', 'Elina', 'Maija', 'Daniel', 'Ibrahim' ]

#print list
print(students)

#insert name Maggie into list at ( index 1, element)
students.insert( 1 , 'Maggie' )

#print list
print(students)

#using a for loop, we want to print item (i) in the list (students)
# for every i in students print in a loop.
for i in students:
    print (i)
    
    

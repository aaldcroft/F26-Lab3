# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Abby Aldcroft 
# Date:Oct 1 2026
# Purpose: 
# Usage: ./lab3f.py

# Follow the specific instructions given in the README.md file
'''
 Fill in the required fields in the comment section.
- Copy the above code in the file `lab3f.py`.
- Print the element `5` from this list. Specify the correct row and column.
- Print the element `2` from this list.
- Print the element `9` from this list.
- Use a for loop and print individual lists from this matrix. 
You need a single for loop. The output should be like this:
'''

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

# element 5 is = to location 
element5 = matrix[1][1]

#print location 
print("the element at second row second column is ",matrix[1][1])

# element 2 is = to location
element2 = matrix [0][1]
#print location
print("The element at first row second column is ",matrix[0][1])


#element 9 is = to location
element9 = matrix [2][2]
#print location
print ("The element in the third column third row is : ",matrix[2][2])

#for loop to print the list items in the matrix , it will print the first row, then second then thrid
for i in matrix:
    print (i)
 
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
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

element5 = matrix[1][1]
print("the element at second row second column is ",matrix[1][1])

for i in matrix:
    print(i)

for i in range(3):
    print(matrix[i])


'''
element2 = matrix [0][1]
print("The element at first row second column is ",matrix[0][1])

for i in matrix:
    print(i)

for i in range(2):
    print(matrix[i])

element9 = matrix [2][2]
print ("The element at the last row last column is : ",matrix[2][2])

for i in matrix:
    print(i)

for i in range(3):
    print(matrix[i])
'''
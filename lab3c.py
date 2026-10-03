# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Abby Aldcroft
# Date:Sept 30, 2026 
# Purpose: Create two lists and join them
# Usage: ./lab3c.py

# Follow the specific instructions given in the README.md file
'''
### lab3c.py
### Creating lists and list concatenation
Lists are constructed with brackets [] and commas separating every element in the list. For example:
```Python
numbers=[1,2,3,4]
mixed_list=[1, "two", 4.5, True]
```
- Fill in the required fields in the comment section
- Create a variable of the type list called `mylist1` and save first three odd numbers (1,3,5) in it.
- Create a second variable of the type list and call it `mylist2`, save first three even numbers (0,2,4) in it.
- Create a third variable called `mylist`. This variable should contain all elements form mylist1 and mylist2.
 Remember you can use + to concatenate lists, just like we did for strings.
- Print the variable `mylist`.
'''
#fist list of numbers (odd)
numbers= [1,5,7]

#second list of number (even)
mixed_list = [0,6,4,]

#third list where bot lists are concatenated.
my_list = numbers+mixed_list

print(my_list)

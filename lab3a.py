# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Abby Aldcroft
# Date: sept. 30, 2026
# Purpose: 
# Usage: ./lab3a.py

#import random and give it a alias here we used 'r' 
import random as r

#set the variable to the sample range of numbers, which is numbers between 1 -100 with 20 steps between each
sequence = r.sample (range(0,100),20)

#printing seqquence here will print the sequence of random numbers.
print("Sequence of random numbers :", sequence)

#sequence.sort() sorts the the random numbers from lowest to highest.
sequence.sort()

#printing sequence will now print the numbers in their ordered sequence.
print("numbers in ordered sequence: ", sequence)
'''
By: ind3x
This script is something of a sustitude cypher but for this part i had to change the index to start at 1
'''

import fidx
from sympy import mod_inverse
#create custom type `list1b` from `list`
fidx.add(list, name='list1')

#add a map int indexes (i -> i-1)
fidx.list1.set_index_map(int, lambda _,i: i-1, override=True)

#create your lists

#numbers that form strings
numbers= fidx.list1([268,413,110,190,426,419,108,229,310,379,323,373,385,236,92,96,169,321,284,185,154,137,186])

#Array of charrecters sustituted by numbers
letters_and_numbers= fidx.list1(['A','B','C','D','E','F','J','H','I','J','K','L','M','N','O','P','Q','R','S',
'T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_'])

print("\nLetters and numbers are:",len(letters_and_numbers))
print("Flag is:", len(numbers), " long\n")

i=1
while i <= len(numbers): 
    mod = numbers[i] % 41
    print(letters_and_numbers[mod_inverse(mod,41)], end='')
    i +=1
print("\n")





'''
By: ind3x
This script is something of a sustitude cypher
'''

#numbers that form strings
cypherMessege= [54,396,131,198,225,258,87,258,128,211,57,235,114,258,144,220,39,175,330,338,297,288]

#Array of charrecters sustituted by numbers
letters_and_numbers= ['A','B','C','D','E','F','J','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W'
                        ,'X','Y','Z','0','1','2','3','4','5','6','7','8','9','_']

print("\nLetters and numbers are:",len(letters_and_numbers)-1)
print("Flag is:", len(cypherMessege)-1, " long\n")

i=0
while i <= len(cypherMessege)-1: 
    mod = cypherMessege[i] % 37 
    print (letters_and_numbers[mod], end='')
    i +=1

print("\n")




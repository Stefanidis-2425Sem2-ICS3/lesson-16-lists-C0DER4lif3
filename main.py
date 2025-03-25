#rylan
#march 20
#starwars magazine quiz 
#this is a quiz that asks starwars based questions and totals up points to get a score out of 200

import random
#create list 

numbers =[]
for i in range (100):
    num=random.randint(0,100)
    numbers.append(num)

print (sum (numbers)/100)
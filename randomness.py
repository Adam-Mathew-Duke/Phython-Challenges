'''
Challenge - Randomness
Define a function, random_number, that takes no parameters. 
The function must generate a random integer 
between 1 and 100, both inclusive, and return it.
Calling the function multiple times 
should (usually) return different numbers.
For example, calling random_number() 
some times might first return 42, then 63, then 1.
'''

# built in Python module
import random

# generate a random number between
# 1 and 100 inclusive
def random_number():
    random_num = random.randint(1,100)
    return(random_num)

print('\n')

# print out 10 random numbers
for index in range(0,10):
    print(str(index+1) + '.\t' + str(random_number()))
    index += 1

# end of code

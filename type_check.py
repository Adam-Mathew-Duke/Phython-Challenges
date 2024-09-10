'''
Challenge - Type check

Write a function named only_ints that takes two parameters.
Your function should return True if both parameters are
integers, and False otherwise.

For example, calling only_ints(1, 2) should return True,
while calling only_ints("a", 1) should return False.
'''

'''
I originally used Try and Except to check if
the param1 and param2 could be converted to
int with int()

This works well for numbers and letters but it
does not work with bool like True and False because
these and 1 and 0.

Checking the data types directly with
type(param1) == int 
is the better solution in this case
'''

# return true if both params are integers
def only_ints(param1,param2):

    if (type(param1) == int and type(param2) == int):
        return True
    else:
        return False

print(only_ints(1,2))

# end of code

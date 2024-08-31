'''
Challenge description:
Write a function named capital_indexes. The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes in the string that have capital letters.
Challenge URL: https://pythonprinciples.com/challenges/Capital-indexes/
'''

'''
Function takes a single parameter and returns a list of indexes
which contain capital letters
'''
def capital_indexes(data):
    
    results_list = []

    '''
    Enumerate over the string parameter that was passed to this function
    idx is the current index of the string
    x is the current char of the string
    Is the current char (x) is an upper case letter then add it to the
    results_list using the append method
    '''
    for idx,x in enumerate(data):
        if str(x) == str(x).upper():
            results_list.append(idx)
            
    return results_list
    
# Function accepts a single string parameter that is a mix of upper and lowercase letters
getlist = capital_indexes("HeLlO")
print(getlist)

# end of code

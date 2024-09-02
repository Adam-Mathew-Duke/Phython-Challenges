'''
Challenge description:
Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''

'''
Return the middle character if the string is an odd length
'''
def mid(input_string):

    string_length = len(input_string)

    if string_length %2 != 0: # odd length
        # Find the middle character using floor division
        return (input_string[string_length//2]) # return middle character
    else: # even length
        return "" # return empty string

print(mid("abc"))
# end of code

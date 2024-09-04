'''
Challenge
Online status. The aim of this challenge is, given a dictionary of people's online status,
to count the number of people who are online.
'''

# list of people (keys) and their online status (values)
statuses_list = {"Alice":"online","Bob":"offline","Eve":"online"}

# return the number of people currently online
def online_count(online_statuses):
    
    count = 0

    for index in online_statuses.values():
        if index == "online":
            count = count + 1

    return(count)

# print out the number of people that are online
print(online_count(statuses_list))

# end of code

def capital_indexes(data):
    results_list = []
    for idx,x in enumerate(data):
        if str(x) == str(x).upper():
            results_list.append(idx)
    return results_list
    
getlist = capital_indexes("HeLlO")
print(getlist)

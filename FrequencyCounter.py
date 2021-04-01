def same(list1, list2):
    if len(list1) != len(list2):
        return False
    frequency_counter1 = {}
    frequency_counter2 = {}
    for val in list1:
        if val not in frequency_counter1:
            frequency_counter1[val] = 1
            continue
        else:
            frequency_counter1[val] = frequency_counter1[val] + 1
        
    for val in list2:
        if val not in frequency_counter2:
            frequency_counter2[val] = 1
            continue
        else:
            frequency_counter2[val] = frequency_counter2[val] + 1
    for key in frequency_counter1.keys():
        if key**2 not in frequency_counter2:
            return False
        if(frequency_counter2[key**2] != frequency_counter1[key]):
            return False
    print(frequency_counter1)
    print(frequency_counter2)
    return True



print(same([1,5,5,2],[25,1,4,25]))
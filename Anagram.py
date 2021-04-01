def same(str1, str2):
    if len(str1) != len(str2):
        return False
    frequency_counter1 = {}
    frequency_counter2 = {}
    for val in str1:
        if val not in frequency_counter1:
            frequency_counter1[val] = 1
            continue
        else:
            frequency_counter1[val] = frequency_counter1[val] + 1

    for val in str2:
        if val not in frequency_counter2:
            frequency_counter2[val] = 1
            continue
        else:
            frequency_counter2[val] = frequency_counter2[val] + 1
    for key in frequency_counter1.keys():
        if key not in frequency_counter2:
            return False
        if frequency_counter2[key] != frequency_counter1[key]:
            return False
    print(frequency_counter1)
    print(frequency_counter2)
    return True


print(same("sea","ase"))
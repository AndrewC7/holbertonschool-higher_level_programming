#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        result = []
        for x in range(len(my_list)):
            if my_list[x] % 2:
                result.append(False)
            else:
                result.append(True)
        return result

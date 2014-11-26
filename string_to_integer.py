#!/usr/bin/python
import math
def atoi(str):
    str = str.strip()
    newstr = []
    for i in range(len(str)):
        if '0'<= str[i]<='9' or (str[i] in ('+', '-') and i == 0):
            newstr.append(str[i])
        else:
            break
    if newstr in ([], ['+'], ['-']):
        return 0
    elif -math.pow(2,31) <= int(''.join(newstr)) <= math.pow(2,31)-1:
        return int(''.join(newstr))
    elif int(''.join(newstr)) > math.pow(2,31)-1:
        return int(math.pow(2,31)-1)
    else:
        return int(-math.pow(2,31))

str = '1234'
print atoi(str)

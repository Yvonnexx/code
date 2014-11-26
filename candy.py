#!/usr/bin/python

def candy(ratings):
    length = len(ratings)
    if length == 0:
        return 0
    candy = [1]*length
    for i in range(1, length):
        if ratings[i] > ratings[i-1]:
            candy.append(candy[i-1] + 1)
    sum = candy[length-1]
    for i in range(length-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candy[i] = max(candy[i], candy[i+1]+1)
        sum += candy[i]
    return sum

ratings = [2,1]
print candy(ratings)

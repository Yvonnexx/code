#!/usr/bin/python

def longest_substring_two(s):
    maxlen = 0
    start = 0
    num = 0
    count_table = [0]*256
    import pdb;pdb.set_trace()
    for i in range(len(s)):
        if count_table[ord(s[i])] == 0:
            num += 1
        count_table[ord(s[i])] += 1
        while num > 2:
            count_table[ord(s[start])] -= 1
            if count_table[ord(s[start])] == 0:
                num -= 1
            start += 1
        maxlen = max(maxlen, i-start+1)
    return maxlen


s = 'eceba'
print longest_substring_two(s)

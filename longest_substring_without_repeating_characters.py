#!/usr/bin/python

def longest_substring(s):
    maxlen = 0
    start = 0
    hashtable = [-1]*256
    for i in range(len(s)):
        if hashtable[ord(s[i])] != -1:
            hashtable[ord(s[start])] += 1
            start += 1
        if i - start + 1 > maxlen:
            maxlen = i - start + 1
        hashtable[ord(s[i])] = i
    return maxlen

s = 'abcabcbb'

print longest_substring(s)

#!/usr/bin/python

def longest_palindrome(s):
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expandAround(s, i, i)
        len2 = expandAround(s, i, i+1)
        length = max(len1, len2)
        if length > end-start:
            start = i - (length-1)/2
            end = i + length/2
    return s[start:end+1]

def expandAround(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

s = 'bb'
print longest_palindrome(s)

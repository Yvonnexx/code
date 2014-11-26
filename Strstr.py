#!/usr/bin/python

def strStr(haystack, needle):
    if not needle:
        return 0
    elif not haystack:
        return -1
    len1 = len(haystack)
    len2 = len(needle)
    if len1 < len2:
        return -1
    for i in range(len1-len2+1):
        j = 0
        k = i
        while j< len2 and haystack[k] == needle[j]:
            j += 1
            k += 1
        if j == len2:
            return i
    return -1

haystack = 'aab'
needle = 'ab'
print strStr(haystack, needle)

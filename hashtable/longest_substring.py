#!/usr/bin/python

class Solution:
    def lengthOfLongestSubstring(self, s):
        list = []
        start = 0
        for start in range(len(s)):
            valuelist = []
            for i in range(start, len(s)+1):
                if i >= len(s):
                    if valuelist:
                        list.append(valuelist[:])
                else:
                    if s[i] not in valuelist:
                        valuelist.append(s[i])
                    else:
                        list.append(valuelist[:])
                        valuelist = [s[i]]
        for a in list:
            print ''.join(a)
        print ' '.join(max(list, key=len))
        return len(max(list, key=len))

    def find(self, s):
        maxlen = 0
        substr = ''
        end = 0
        for start in range(len(s)):
            if s[start] not in substr:
                substr += s[start]
            else:
                maxlen = max(maxlen, len(substr))
                while s[end] != s[start]:
                    end += 1
                end = end + 1
                substr = s[end:start+1]
        return max(maxlen, len(substr))

solution = Solution()
s = 'qpxrjxkltzyx'
print solution.find(s)
#print solution.lengthOfLongestSubstring(s)

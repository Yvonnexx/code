#!/usr/bin/python

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        len_strs = len(strs)
        if len_strs == 0:
            return ''
        if len_strs == 1:
            return strs[0]
        lengths = [len(s) for s in strs]
        common_prefix = ''
        for i in range(min(lengths)):
            temp = strs[0][i]
            for j in range(1, len_strs):
                if strs[j][i] != temp:
                    return common_prefix
            common_prefix += temp
        return common_prefix

s = Solution()
strs = ['abc', 'ab', 'a']
print s.longestCommonPrefix(strs)

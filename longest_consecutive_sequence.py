#!/usr/bin/python

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dict = {x:False for x in num}
        maxlen = -1
        for i in dict:
            if not dict[i]:
                curr = i + 1
                lenright = 0    
                lenleft = 0
                while curr in dict:
                    dict[curr] = True
                    lenright += 1
                    curr += 1
                curr = i - 1
                while curr in dict:
                    dict[curr] = True
                    curr -= 1
                    lenleft += 1
                maxlen = max(maxlen, lenleft + lenright + 1)
        return maxlen 

if __name__ == "__main__":
    s = Solution()
    num = [100, 4, 200, 1, 3 ,2]
    #print s.longestConsecutive(num)
    print s.longest(num)

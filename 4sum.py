#!/usr/bin/python

class Solution:
    # @return a list of lists of length 4
    def fourSum(self, num, target):
        length = len(num)
        res = set()
        dict = {}
        if length < 4:
            return []
        for i in range(length):
            for j in range(i+1, length):
                if num[i]+num[j] not in dict:
                    dict[num[i]+num[j]] = [(i,j)]
                else:
                    dict[num[i]+num[j]].append((i,j))
        for i in range(length):
            for j in range(i+1, length-2):
                tmp = target - num[i] - num[j]
                if tmp in dict:
                    for k in dict[tmp]:
                        if k[0] > j:
                            res.add((num[i], num[j], num[k[0]], num[k[1]]))
        return [list(i) for i in res]
    
if __name__ == "__main__":
    s = Solution()
    num = [1, 0, -1, 0, -2, 2]
    target = 0
    print s.fourSum(num, target)

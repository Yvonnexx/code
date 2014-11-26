#!/usr/bin/python

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        res = []
        list = []
        visited = [0]*len(num)
        self.generate(res, list, visited, num)
        return res
    def generate(self, res, list, visited, num):
        if len(list) == len(num):
            res.append(list[:])
            return
        for i in range(len(num)):
            if visited[i] == 1 or (i != 0 and num[i] == num[i-1] and visited[i-1] == 0):
                continue
            visited[i] = 1
            list.append(num[i])
            self.generate(res, list, visited, num)
            list.pop()
            visited[i] = 0

if __name__ == "__main__":
    s = Solution()
    num = [1,1,2]
    print s.permuteUnique(num)

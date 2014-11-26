#!/usr/bin/python

def twoSum(num, target):
    dict = {}
    for i in xrange(len(num)):
        if (target-num[i]) in dict:
            return (dict[target-num[i]] + 1, i+1)
        else:
            dict[num[i]] = i

def twoSumii(num, target):
    i = 0
    j = len(num) - 1
    while i < len(num) and j > 0:
        if num[i] + num[j] > target:
            j -= 1
        elif num[i] + num[j] < target:
            i += 1
        else:
            return (i+1, j+1)

class TwoSum():
    def __init__(self):
        self.dict = {}

    def add(self, input):
        if input in self.dict:
            self.dict[input] += 1
        else:
            self.dict[input] = 1

    def find(self, value):
        for item in self.dict:
            if value - item == item:
                if self.dict[item] >= 2:
                    return True
            elif value - item in self.dict:
                return True
        return False

if __name__ == "__main__":
    """
    num = [2,7,11,15]
    target = 9
    print twoSum(num, target)
    print twoSumii(num, target)
    """
    s = TwoSum()
    s.add(2)
    s.add(1)
    s.add(5)
    print s.find(4)


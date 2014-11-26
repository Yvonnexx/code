#!/usr/bin/python
import collections

def ladderLength(start, end, dict):
    dict.append(start)
    length = len(start)
    queue = collections.deque([(start, 1)])
    while queue:
        curr = queue.popleft()
        currword = curr[0]
        currlen = curr[1]
        if currword == end:
            return currlen
        for i in range(length):
            part1 = currword[:i]
            part2 = currword[i+1:]
            for j in 'abcdefghijklmnopqrstuvwxyz':
                if currword[i] != j:
                    nextword = part1 + j + part2
                    if nextword in dict:
                        queue.append((nextword, currlen+1))
                        dict.remove(nextword)
    return 0

start = 'hit'
end = 'cot'
dict = set('hot', 'dot', 'dog', 'lot', 'log')
print ladderLength(start, end, dict)

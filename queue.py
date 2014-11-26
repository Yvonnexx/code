#!/usr/bin/python

def queueappend(obj):
    s = []
    s.append(obj)

def queuepop():
    if not s2:
        if not s1:
            return None
        while s1:
            s2.append(s1.pop())
    return s2.pop()

if __name__ == "__main__":
    obj1 = 1
    queueappend(obj1)
    obj2 = 2
    queueappend(obj2)
    print queuepop()

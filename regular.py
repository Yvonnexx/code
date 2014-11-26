#!/usr/bin/python

def isMatch(s, p):
    """
    >>> isMatch('aa', 'a')
    False
    >>> isMatch('aa', 'aa')
    True
    >>> isMatch('aaa', 'aa')
    False
    >>> isMatch('aa', 'a*')
    True
    >>> isMatch('aa', '.*')
    True
    >>> isMatch('ab', '.*')
    True
    >>> isMatch('aab', 'c*a*b')
    True
    """
    import pdb;pdb.set_trace()
    if not s:
        return not p 
    if not p:
        return not s 
    lens = len(s)
    lenp = len(p)
    if lenp == 0:
        return lens == 0
    pdb.set_trace()
    if lenp == 1:
        if len(s) == 1 and p[0] == '.':
            return True
        if len(s) == 1 and p[0] == s[0]:
            return True
        else:
            return False
    if p[1] != '*':
        if lens > 0 and (p[0] == s[0] or p[0] == '.'):
            return isMatch(s[1:], p[1:])
        return False
    else:
        # import pdb; pdb.set_trace()
        while (lens > 0) and (p[0] == s[0] or p[0] == '.'):
            if isMatch(s,p[2:]):
                return True
            s = s[1:]
            lens = len(s)
        return isMatch(s, p[2:])

if __name__ == '__main__':
    import doctest
    doctest.testmod()

#!/usr/bin/python

def isMatch(s, p):
    s_curr = 0
    p_curr = 0
    star = -1
    ss = 0
    import pdb;pdb.set_trace()
    while s_curr < len(s):
        if p_curr < len(p) and (s[s_curr] == p[p_curr] or p[p_curr] == '?'):
            s_curr = s_curr + 1
            p_curr = p_curr + 1
            continue
        if p_curr < len(p) and p[p_curr] == '*':
            ss = s_curr
            star = p_curr
            p_curr = p_curr + 1
            continue
        if star != -1:
            p_curr = star + 1
            ss += 1
            s_curr = ss
            continue
        return False
    while p_curr < len(p) and p[p_curr] == '*':
        p_curr += 1
    return p_curr == len(p)
#print isMatch('', '*')
#print isMatch('aa', 'a')
#print isMatch('aa', 'aa')
#print isMatch('aaa', 'aa')
print isMatch('aa', '*')
#print isMatch('aa', 'a*')
#print isMatch('ab', '?*')
#print isMatch('aab', 'c*a*b')

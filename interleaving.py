#!/usr/bin/python

def isInterleave(s1, s2, s3):
    len1 = len(s1)
    len2 = len(s2)
    len3 = len(s3)
    if len1 + len2 != len3:
        return False
    dp = [[0 for i in range(len2+1)] for j in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i > 0 and dp[i-1][j] == i-1+j and s1[i-1] == s3[i+j-1]:
                dp[i][j] = i+j
            if j > 0 and dp[i][j-1] == i+j-1 and s2[j-1] == s3[i+j-1]:
                dp[i][j] = i+j
    return dp[len1][len2] == len3


s1 = 'aabcc'
s2 = 'dbbca'
#s3 = 'aadbbcbcac'
s3 = 'aadbbbaccc'
print isInterleave(s1, s2, s3)

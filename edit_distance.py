#!/usr/bin/python

def minDistance(word1, word2):
    m = len(word1) + 1
    n = len(word2) + 1
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        dp[0][i] = i
    for i in range(m):
        dp[i][0] = i
    for i in range(1, m):
        for j in range(1, n):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1]+1
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i][j])

    return dp[m-1][n-1]


word1 = 'cat'
word2 = 'bcy'
print minDistance(word1, word2)

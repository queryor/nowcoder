# Given a string S and a string T, count the number of distinct subsequences of S which equals T.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# Example 1:

# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:

# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)

# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# Example 2:

# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:

# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)

# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ## DP 
        n = len(s)
        m = len(t)
        if n<m:
            return 0
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(n):
            dp[0][i]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[j-1]==t[i-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j]=dp[i][j-1]
        return dp[m][n]
        
        
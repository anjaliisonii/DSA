1.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(n,m,s1,s2,dp):
            if n==0 or m==0:
                return 0
            if dp[n][m]!=-1:
                return dp[n][m]
            if s1[n-1]==s2[m-1]:
                dp[n][m]=1+lcs(n-1,m-1,s1,s2,dp)
                return dp[n][m]
            else:
                dp[n][m]=max(lcs(n-1,m,s1,s2,dp),lcs(n,m-1,s1,s2,dp))
                return dp[n][m]
        n=len(text1)
        m=len(text2)
        dp=[[-1 for i in range (m+1)]for j in range (n+1)]
        return lcs(n,m,text1,text2,dp)
2.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[0 for i in range (m+1)]for j in range (n+1)]
        for i in range (1,n+1):
            for j in range (1,m+1):
                if i==0 or j==0:
                     return 0
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[n][m]

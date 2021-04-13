def solve(i,j,m,n,dp):
    if i<m and j<n and i>=0 and j>=0:
        if dp[i][j]==-1:
            dp[i][j]=solve(i-1,j,m,n,dp)+solve(i,j-1,m,n,dp)
        return dp[i][j]
    else:
        return 0
class Solution(object):
    def uniquePaths(self, m, n):
        dp=[]
        for i in range(m+1):
            dp.append([-1]*(n+1))
        dp[0][0]=1
        return solve(m-1,n-1,m,n,dp)
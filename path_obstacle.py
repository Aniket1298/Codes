def solve(i,j,m,n,dp,l):
    if i<m and j<n and i>=0 and j>=0:
        if l[i][j]==1:
            return 0
        if dp[i][j]==-1:
            dp[i][j]=solve(i-1,j,m,n,dp,l)+solve(i,j-1,m,n,dp,l)
        return dp[i][j]
    else:
        return 0

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp=[]
        for i in range(m+1):
            dp.append([-1]*(n+1))
        dp[0][0]=1
        return solve(m-1,n-1,m,n,dp,obstacleGrid)
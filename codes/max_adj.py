def solve(l,i,dp):
    if i<0:
        return 0
    elif dp[i]==-1:
        dp[i]=max(solve(l,i-2,dp)+l[i],solve(l,i-1,dp),l[i])
    return dp[i]
class Solution:
    def solve(self, nums):
        l=nums
        if len(l)==0:
            return 0
        if len(l)==1:
            return l[0]
        dp=[-1]*(len(l)+3)
        dp[0]=l[0]
        dp[1]=max(l[0],l[1])
        solve(l,len(l)-1,dp)
        return max(0,dp[len(l)-1])
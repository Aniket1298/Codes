def solve(i,l,ans,dp,out):
    if i>=len(l)-1:
        return ans
    elif dp[i]!=-1:
        return dp[i]
    else:
        j=i+1
        while j<len(l):
            op1=solve(j,l,ans,dp,out)+ans
            op2=solve(j+1,l,ans+l[j]-l[i],dp,out)
            dp[i]=max(ans,ans+l[j]-l[i])
            j+=1
            return dp[i]
class Solution(object):
    def maxProfit(self, prices):
        l=prices
        dp=[-1]*(len(l)+3)
        solve(0,l,0,dp,[0])
        s=0
        ans=0
        for i in dp:
            s+=i
            ans=max(ans,s)
        return ans
            
        
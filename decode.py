def solve(s,i,dp):
    ans=0
    if dp[i]!=-1:
        return dp[i]
    if i==0:
        ans= 1
    elif i==1:
        if int(s[0:2]) in [10,20]:
            ans=1
        elif int(s[0:2]) in [30,40,50,60,70,80,90]:
            ans=0
            dp[0]=0
            dp[1]=0
        elif int(s[0]+s[1])>26:
            ans= 1
        else:
            ans= 2
    elif s[i]=='0':
        if int(s[i-1])>2:
            dp[i]=0
            dp[i-1]=0
            ans=0
        else:
            ans=solve(s,i-2,dp)
    elif s[i-1]=='0':
        ans=solve(s,i-1,dp)
    else:
        if int(s[i-1]+s[i])>26:
            ans=solve(s,i-1,dp)
        else:
            ans=solve(s,i-1,dp)+solve(s,i-2,dp)
    dp[i]=ans
    return ans

class Solution(object):
    def numDecodings(self, s):
        if '00' in s or s[0]=='0':
            return 0
        dp=[-1]*(len(s)+2)
        return solve(s,len(s)-1,dp)
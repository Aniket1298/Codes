n=input()
dp=[9999999]*(n+20)
dp[0]=0
for i in xrange(1,n+1):
    x=i
    while x>0:
        dig = x%10
        if dig!=0:
            dp[i]=min(dp[i],dp[i-dig]+1)
        x/=10
print dp[n]
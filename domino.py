def solve(n):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
n,m=map(int,raw_input().split())
f2=solve(n)
dp=[0]*(m+1)
if n%2==0:
    dp[1]=1
for i in range(2,m+1):
    if n%2==0:
        dp[i]+=dp[i-1]
        dp[i]+=dp[i-2]+f2
    else:
        dp[i]+=dp[i-2]+f2
print f2,dp
print dp[m]


n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
dp=[]
for i in range(251):
    dp.append([0]*255)
for i in range(k):
    for j in range(n+1):
        if j==0:
            dp[i][j]=1
        else:
            dp[i][j]=dp[i][j-l[i]]+dp[i-1][j]
print dp[k-1][n]

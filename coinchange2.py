M=10**9 + 7
n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
dp=[]
for i in xrange(n+1):
    dp.append([0]*(k+1))
for i in range(n):
    for money in range(k+1):
        if money==0:
            dp[i][money]=1
        else:
            #print money,l[i]
            if i!=0:
                dp[i][money]+=dp[i-1][money]
            if money>=l[i]:
                dp[i][money]+=dp[i][money-l[i]]
            #print "TANA",dp[i][money]
            dp[i][money]%=M

print dp[n-1][k]
n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
dp=[1e7]*(k+1)
for i in l:
    if i<len(dp):
        dp[i]=1
i=0

while i<n:
    money=0
    while money<=k:
        if l[i]<=money:
            #print money,l[i],money-l[i],dp[money-l[i]],dp[money]
            dp[money]=min(dp[money-l[i]]+1,dp[money])
        money+=1
    i+=1
#print dp
if dp[k]!=1e7:
    print dp[k]
else:
    print -1
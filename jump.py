from sys import stdin
for _ in range(input()):
    n=input()
    l=map(int,stdin.readline().split())
    dp=[-1]*(n+2)
    ans=0
    i=0
    s=sum(l)
    mx=0
    i=n-1
    while i>=0:
        if dp[i]!=-1:
            ans=dp[i]
        else:
            j=i
            ans=0
            flag=0
            while j<n and flag==0:
                if dp[j]==-1:
                    ans+=l[j]
                    j+=l[j]
                else:
                    ans+=dp[j]
                    flag=1
                    break
            dp[i]=ans
        mx=max(mx,dp[i])
        i-=1
    print mx
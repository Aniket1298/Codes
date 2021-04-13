#Python 2.7.17
from sys import stdin
import array as L
n,m=map(int,stdin.readline().split())
l=map(int,stdin.readline().split())
dp=[L.array('L',[0]*(m+1)) for i in xrange(n+1)]
i=0
M=pow(10,9)+7
while i<n:
    if i==0:
        if l[i]==0:
            j=1
            while j<=n:
                dp[i][j]=1
                j+=1
        else:
            dp[i][l[i]]=1
    else:
        if l[i]==0:
            j=1
            while j<=m:
                dp[i][j]+=dp[i-1][j]
                if j-1>0:
                    dp[i][j]+=dp[i-1][j-1]
                if j+1<=m:
                    dp[i][j]+=dp[i-1][j+1]
                dp[i][j]%=M
                j+=1

        else:
            j=l[i]
            dp[i][j]+=dp[i-1][j]

            if j-1>=1:
                dp[i][j]+=dp[i-1][j-1]
            if j+1<=m:
                dp[i][j]+=dp[i-1][j+1]
            dp[i][j]%=M
    i+=1
print sum(dp[n-1])%M
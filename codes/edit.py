a=raw_input()
b=raw_input()
dp=[]
n,m=len(a),len(b)
i=0
while i<n+1:
    dp.append([5001]*len(b))
    i+=1
i=0
if a[0]==b[0]:
    dp[0][0]=0
else:
    dp[0][0]=1
i=0
while i<len(a):
    j=0
    while j<len(b):
        if i==0 and j==0:
            #print i,j,'J',a[i],b[j]
            if a[i]==b[j]:
                dp[i][j]=0
            else:
                dp[i][j]=1
        elif i==0:
            if a[i]==b[j]:
                dp[i][j]=j
            else:
                dp[i][j]=j+1
        elif j==0:
            if a[i]==b[j]:
                dp[i][j]=i
            else:
                dp[i][j]=i+1
        else:
            if a[i]==b[j]:
                dp[i][j]=min(dp[i][j],dp[i-1][j-1])
            else:
                dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,1+dp[i-1][j-1])
        j+=1
    i+=1
print dp[n-1][m-1]
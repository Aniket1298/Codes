## Upper Bound in Python 
```
def upper_bound(l,n):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)/2
        if l[mid]<n:
            low=mid+1
        elif l[mid]>n:
            high=mid-1
        else:
            break
    if l[mid]<=n:
        mid+=1
    return min(len(l)-1,mid)
```
## Transpose a Matrix
```
list(zip(*matrix))
```
## Coin Change
```
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
            dp[money]=min(dp[money-l[i]]+1,dp[money])
        money+=1
    i+=1
if dp[k]!=1e7:
    print dp[k]
else:
    print -1
```
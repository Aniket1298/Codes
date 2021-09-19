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
## Number of paths in a matrix
```
def find(i,j):
    if i==x and j==y:
        return
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0
    if dp[i][j]:
        return dp[i][j]
    dp[i][j]= find(i-1,j,x,y)+find(i,j-1,x,y)
    return dp[i][j]
n,m=3,3
dp=[[0]*(m+1) for i in range(n+1)]
print find(n,m)
```
## Amazon fulfillment Center
```
import heapq
def solve(l):
    heapq.heapify(l)
    ans=0
    while len(l)>1:
        a,b=heapq.heappop(l),heapq.heappop(l)
        ans+=a+b
        heapq.heappush(l,a+b)
    return ans
print solve([8,4,6,12])
```
## Amazon Air route
```
def solve(F,B,T):
    mx=0
    ans=[]
    F.sort(key=lambda x:x[1])
    B.sort(key=lambda x:x[1])
    for index,item in F:
        start=0
        end=len(B)-1
        search=T-item
        last=0
        while start<=end:
            mid=(start+end)/2
            if B[mid][1]>search:
                end=mid-1
            elif B[mid][1]<search:
                start=mid+1
            else:
                break
        cur=item+B[mid][1]
        if cur>mx and cur<=T:
            ans=[[index,B[mid][0]]]
            mx = cur
        elif cur==mx:
            ans.append([index,B[mid][0]])
    if len(ans)==0:
        return []
    return ans

print solve([(1,8),(2,15),(3,9)],
	 [(1,8),(2,11),(3,12)], 20)
```

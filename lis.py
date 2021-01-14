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
def lis(l):
    inf=999999999999999
    d=[inf]*(len(l)+1)
    d[0]=-inf
    n=len(l)
    for i in range(n):
        j=upper_bound(d,l[i])
        if d[j-1]<l[i] and l[i]<d[j]:
            d[j]=l[i]
    ans=1
    for i in range(len(d)):
        if d[i]!=inf:
            ans=i
    return  ans

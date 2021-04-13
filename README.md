## Upper Bound Python 
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
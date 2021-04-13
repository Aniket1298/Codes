from sys import stdin
def get(l,k):
    ans=0
    if len(l)<3:
        for i in l:
            if i>k:
                ans+=1
        return ans
    i,j=0,len(l)-1
    while i<=j:
        mid=(i+j)/2
        if l[mid]>k:
            j=mid-1
        elif l[mid]<k:
            i=mid+1
        else:
            break
    while mid<len(l) and l[mid]<=k:
        mid+=1
    return len(l)-mid
def query(v,start,end,left,right,k):
    print v,start,end,left,right,k
    print nth
    nth[0]+=1
    if nth>100:
        return
    v,start,end,left,right,k
    if start>end:
        return 0
    if start==left and right==end:
        return get(t[v],k)
    mid=(left+right)/2
    x=query(v*2,start,min(mid,end),left,mid,k)
    y=query(v*2+1,max(left,start),end,mid+1,right,k)
    return x+y
def merge(a,b):
    temp=[0]*(len(a)+len(b))
    k=0
    i,j=0,0
    while i<len(a) or j<len(b):
        if i<len(a) and j<len(b):
            if a[i]<b[j]:
                temp[k]=a[i]
                i+=1
                k+=1
            else:
                temp[k]=b[j]
                j+=1
                k+=1
        elif i<len(a):
            temp[k]=a[i]
            k+=1;i+=1;
        elif j<len(b):
            temp[k]=b[j]
            k+=1;j+=1;
    return temp
def build(v,left,right):
    if left==right:
        t[v]=[l[left]]
    else:
        mid=(left+right)/2
        build(2*v,left,mid)
        build(2*v+1,mid+1,right)
        t[v]=merge(t[v*2],t[v*2+1])
t=[0]*(100)
n=input()
l=map(int,stdin.readline().split())
build(1,0,n-1)
for _  in range(input()):
    a,b,k=map(int,raw_input().split())
    print query(1,a-1,b-1,0,n-1,k)

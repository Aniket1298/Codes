def g(i,j):
    return str(i)+ ' '+str(j)
def check(i,j,n,f):
    cnt=0
    try:
        if i+1<n and visited[i+1][j]==1 and (g(i,j) in d[g(i+1,j)] or g(i+1,j) in d[g(i,j)]):
            cnt+=1
    except KeyError:
        pass
    try:
        if i-1>=0 and visited[i-1][j]==1 and (g(i,j) in d[g(i-1,j)] or g(i-1,j) in d[g(i,j)]):
            cnt+=1
    except KeyError:
        pass
    try:
        
        if j+1<n and visited[i][j+1]==1 and (g(i,j) in d[g(i,j+1)] or g(i,j+1) in d[g(i,j)]):
            cnt+=1
    except KeyError:
        pass
    try:
        if j-1>=0 and visited[i][j-1]==1 and (g(i,j) in d[g(i,j-1)] or g(i,j-1) in d[g(i,j)]):
            cnt+=1
    except KeyError:
        pass
    if cnt==f:
        return True
    return False
n,k=list(map(int,input().split()))
l=[]
total=n*n
visited=[]
for i in range(n):
    visited.append([1]*n)
d={}
for _ in range(k):
    a,b,c,z=list(map(int,input().split()))
    a-=1;b-=1;c-=1;z-=1;
    x,y=str(a)+ ' '+str(b),str(c)+ ' '+str(z)
    #print(x,y)
    try:
        d[x].append(y)
    except KeyError:
        d[x]=[y]
    try:
        d[y].append(x)
    except KeyError:
        d[y]=[x]
for friends in range(4,0,-1):
    for i in range(n):
        for j in range(n):
            if visited[i][j]==1 and check(i,j,n,friends):
                visited[i][j]=0
ans=0
for i in visited:
    ans+=sum(i)
print(ans)
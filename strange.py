def solve(n,x):
    ans=0
    if n%x==0:
        ans=n + x*solve(n/x,x)[0]
        return [ans,0]
    else:
        ans=n
        return [ans,1]
for _ in range(input()):
    a,x=map(int,raw_input().split())
    l=map(int,raw_input().split())
    bl=[0]
    ans=0
    for i in l:
        ans+=solve(i,x)
    print ans
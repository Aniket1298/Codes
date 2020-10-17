
for _ in range(input()):
    a,b,x,y,n=map(int,raw_input().split())
    if a<b:
        b,a=a,b
        x,y=y,x
    ans=[]
    d=min(b-y,n)
    c=min(a-x,n-d)
    ans.append((a-c)*(b-d))
    c=min(a-x,n)
    d=min(b-y,n-c)
    ans.append((a-c)*(b-d))
    print min(ans)
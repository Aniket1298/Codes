for _ in range(input()):
    n,x,y=map(int,raw_input().split())
    if n==2:
        print x,y
    else:
        t=n
        x,y=min(x,y),max(x,y)
        d=-1
        while (y-x)%(n-1)!=0:
            n-=1
        d=(y-x)/(n-1)
        l=[x]
        x+=d
        while x<=y:
            l.append(x)
            x+=d
        x=l[0]-d
        while x>0 and len(l)<t:
            l.append(x)
            x-=d
        x=y
        while len(l)<t:
            x+=d
            l.append(x)
        for i in  l:
            print i,
        print   
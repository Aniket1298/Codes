import math
for _ in range(input()):
    a,b=map(int,raw_input().split())
    d=abs(b-a)
    n=10
    ans=0
    while d>0:
        x=d/n
        if n!=0:
            ans+=d/n
            d=d%n
        n-=1
    print ans
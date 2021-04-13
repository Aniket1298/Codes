# cook your code here
import math
for _ in range(input()):
    n,x=map(int,raw_input().split())
    l=map(int,raw_input().split())
    mx=0
    for a in l:
        if a%x==1:
            mx+=1
        mx+=a/x
    s=sum(l)
    mn=s/x
    if s%x==1:
        mn+=1
    print mn,mx
    
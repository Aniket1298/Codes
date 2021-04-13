for _ in range(input()):
    a,b,c,d=map(int,raw_input().split())
    dis=abs(c-a)+abs(d-b)
    if a==c or b==d:
        print dis+2
    else:
        print dis
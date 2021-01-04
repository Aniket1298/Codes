for _ in range(input()):
    n=input()
    l=map(int,raw_input().split())
    a,b=l.count(2),l.count(1)
    if sum(l)%2==1 or b%2==1:
        print "NO"
    else:
        if b==0 and a%2==1:
            print "NO"
        else:
            print "YES"
        
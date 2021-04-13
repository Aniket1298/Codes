def solve(a,b):
    if a%2==0:
        return 2*solve(a/2,b)
    elif b%2==0:
        return 2*solve(a,b/2)
    else:
        return 1
for _ in range(input()):
    a,b,n=map(int,raw_input().split())
    if solve(a,b)>=n:
        print "YES"
    else:
        print "NO"
    
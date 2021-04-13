for _ in range(input()):
    n=input()
    l=map(int,raw_input().split())
    cnt=0
    for i in range(n):
        if l[i]==i+1:
            cnt+=1
    if cnt==n:
        print 0
    elif cnt==0:
        print 1
    else:
        i=0
        cnt=0
        while i<len(l) and l[i]==i+1:
            i+=1
        n-=1
        while n>0 and l[n]==n+1:
            n-=1
        while i<=n:
            if l[i]==i+1:
                cnt+=1
            i+=1
        if cnt==0:
            print 1
        else:
            print 2
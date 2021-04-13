from sys import stdin
for _ in range(input()):
    n=input()
    l=map(int,stdin.readline().split())
    a=[]
    b=[]
    for i in l:
        if i%2==0:
            a+=[i]
        else:
            b+=[i]
    a.sort(reverse=True)
    b.sort(reverse=True)
    i,j=0,0
    bob,alice=0,0
    for x in range(n):
        if x%2==0:
            if i<len(a) and j<len(b):
                if a[i]>b[j]:
                    alice+=a[i]
                    i+=1
                else:
                    j+=1
            elif i<len(a):
                alice+=a[i]
                i+=1
            elif j<len(b):
                j+=1
        else:
            if i<len(a) and j<len(b):
                if a[i]<b[j]:
                    bob+=b[j]
                    j+=1
                else:
                    i+=1
            elif j<len(b):
                bob+=b[j]
                j+=1
            elif i<len(a):
                i+=1
    if bob>alice:
        print "Bob"
    elif bob==alice:
        print "Tie"
    if alice>bob:
        print "Alice"
from sys import stdin
_=input()
while _:
    n,m=map(int,stdin.readline().split())
    l=map(int,stdin.readline().split())
    d={}
    i=0
    while i<n:
        d[l[i]%m]=0
        i+=1
    i=0
    while i<n:
        d[l[i]%m]=0
        i+=1
    i=0
    ans=True
    while i<n:
        if l[i]%m==0:
            l[i]=True
        else:
            x=l[i]*2
            r=1<<30
            flag=False
            while x<r and flag==False:
                if x%m==0:
                    l[i]=True
                    flag=True
                x<<=1
            if flag==False:
                ans=False
                break
        i+=1
    if ans==True:
        i=0
        while i<n:
            if l[i]!=True:
                z=l[i]%m
                try:
                    if d[m-z]!=0:
                        d[z]-=1
                        l[i]=True
                except KeyError:
                    pass
                ans=l[i]
            if ans==False:
                break
            i+=1
    if ans:
      print "YES"
    else:
      print "NO"
    _-=1

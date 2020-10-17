an=[0]
def count(a, b):
    ans=0
    for i in range(len(a)):
        if a[i]==b[0]:
            ans+=a[i+1:].count(b[1])
    return ans
n,k=map(int,raw_input().split())
a=raw_input()
b=raw_input()
l=[]
for i in a:
    l.append(i)
a=l
i=0
j=n-1
while k>0 and i<j:
    if a[i]!=a[0] and a[i]!=b[1]:
        a[i]=b[0]
        k-=1
    i+=1
    an[0]=max(an[0],count(a,b))
        a[j]=b[1]   
    if a[j]!=b[1] and a[j]!=b[0]:
        k-=1
    j-=1
    an[0]=max(an[0],count(a,b))
print an[0]
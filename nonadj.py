count=0
n=1
l=[0]*10
while n<100:
    s=str(n)
    flag=1
    for i  in range(len(s)-1):
        if s[i]==s[i+1]:
            flag=0
            break
    if flag:
        count+=1
        l[n%10]+=1
    n+=1
print l
print count
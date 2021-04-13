def maxsub(l):
    dp=[0]
    if l[0]>=0:
        dp.append(l[0])
    else:
        dp.append(0)
    for i in range(1,len(l)):
        if l[i]>0:
            dp.append(max(dp[-1],dp[-2]+l[i]))
        else:
            dp.append(dp[-1])
    if dp[-1]>max(l):
        return dp[-1]
    else:
        return max(l)
n=input()
l=map(int,raw_input().split())
print maxsub(l)
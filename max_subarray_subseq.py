def kadanes(l):
    ans=l[0]
    max_till=l[0]
    for i in range(1,len(l)):
        if max_till+l[i]>0:
            max_till+=l[i]
        else:
            max_till=l[i]
        ans=max(ans,max_till,l[i],l[0])
    return ans
for _ in range(input()):
    n=input()
    l=map(int,raw_input().split())
    print kadanes(l),
    max_subseq=0
    for i in l:
        if i>0:
            max_subseq+=i
    if max_subseq==0 and 0 not in l:
        max_subseq=max(l)
    print max_subseq
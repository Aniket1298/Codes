def solve(s,i):
    ans=0
    if i==0:
        ans= 1
    elif i==1:
        if int(s[0]+s[1])>26:
            ans= 1
        else:
            ans= 2
    else:
        if int(s[i-1]+s[i])>26:
            ans= solve(s,i-1)
        else:
            ans= solve(s,i-1)+1
    return ans
print solve("226",2)
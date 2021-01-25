M=10**9 + 7
n=input()
dp=[1,2,4,8,16,32]
if n<7:
    print dp[n-1]
    exit()
n-=6
while n>0:
    i=len(dp)-1
    s=0
    for i in range(1,7):
        s+=dp[-i]
    s%=M
    dp.append(s)
    dp=dp[1:]
    n-=1
print dp[-1]

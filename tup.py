prime=[1]*(1000001)
n=3
primes=[2]
while n<1000000:
    if prime[n]==1:
        primes.append(n)
        x=n+n
        while x<1000000:
            prime[x]=0
            x+=n
    n+=1
ans=[0]*(1000001)
ans[5]=1
cnt=0
i=1
while i<len(primes) and primes[i]+2<=1000000:
    cnt+=1
    ans[primes[i]+2]=cnt
    i+=1
for i in range(5,len(ans)):
    ans[i]=max(ans[i],ans[i-1])
for _ in range(input()):
    n=input()
    print ans[n]
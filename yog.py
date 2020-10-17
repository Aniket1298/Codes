n=input()
a=map(int,raw_input().split())
b=map(int,raw_input().split())
c=map(int,raw_input().split())
d=map(int,raw_input().split())
ans=0
for i in range(n):
    for j in range(n):
        ans=max(ans,abs(a[i]-a[j])+abs(b[i]-b[j])+abs(c[i]-c[j])+abs(d[i]-d[j])+abs(i-j))
print ans
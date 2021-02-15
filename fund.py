
def dfs(node):
  s[0]+=l[node]
  nodes.append(node)
  visited[node]=1
  for x in g[node]:
    if visited[x]==0:
      dfs(x)
n=int(input())
l=[0]+list(map(int,input().split()))
g=[[] for i in range(n+100)]
q=int(input())
for i in range(q):
  a,b=list(map(int,input().split()))
  g[a].append(b)
  g[b].append(a)
visited=[0]*(n+100)
ans=[]
max_funds=0
i=1
s=[0]
while i<=n:
  if visited[i]==0:
    nodes=[]
    s[0]=0
    dfs(i)
    if s[0]>max_funds:
      max_funds=s[0]
      ans=nodes[::]
    elif s[0]==max_funds and len(ans)>len(nodes):
      ans=nodes[::]
  i+=1
ans.sort()
print (" ".join(str(x) for x in ans))
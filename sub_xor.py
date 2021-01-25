class Node:
    def __init__(self):
        self.left=None
        self.right=None
class Trie:
    def __init__(self):
        self.head=Node()
    def insert(self,n):
        curr=self.head
        for i in xrange(31,-1,-1):
            b=(n>>i)&1
            if b==0:
                if (not curr.left):
                    curr.left=Node()
                curr=curr.left
            else:
                if (not curr.right):
                    curr.right=Node()
                curr=curr.right
    def query(self,n):
        curr=self.head
        xor=0
        for i in xrange(31,-1,-1):
            b=(n>>i)&1
            if b==0:
                if curr.right:
                    xor+=(1<<i)
                    curr=curr.right 
                else:
                    curr=curr.left
            else:
                if curr.left:
                    xor+=(1<<i)
                    curr=curr.left 
                else:
                    curr=curr.right
        return xor
n=input()
l=map(int,raw_input().split())
T=Trie()
pre=0
ans=0
for i in l:
    pre^=i
    T.insert(pre)
    ans=max(pre,ans,T.query(pre))
print ans
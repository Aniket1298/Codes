ans=[['()']]
for i in range(2,9):
    last=ans[-1]
    t=[]
    for s in last:
        x=''
        for i in range(len(s)):
            t.append(x+'()'+s[i:])
            x+=s[i]
    t=list(set(t))
    ans.append(t)
class Solution(object):
    def generateParenthesis(self, n):
        return ans[n-1]
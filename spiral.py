def solve(i,j,l,ans,d):
    ans.append(l[i][j])
    l[i][j]=101
    if len(ans)==len(l)*len(l[0]):
        return ans
    if d=="right":
        if j+1<len(l[0]):
            if l[i][j+1]<101:
                solve(i,j+1,l,ans,d)
            else:
                d="down"
                solve(i+1,j,l,ans,d)
        else:
            d="down"
            solve(i+1,j,l,ans,d)
    elif d=="down":
        if i+1<len(l):
            if l[i+1][j]<101:
                solve(i+1,j,l,ans,d)
            else:
                solve(i,j-1,l,ans,"left")    
        else:
            solve(i,j-1,l,ans,"left")
    elif d=="left":
        if j>0 and l[i][j-1]<101:
            solve(i,j-1,l,ans,d)
        else:
            solve(i-1,j,l,ans,"up")
    else:
        #print "HERE",i,j,l
        if i>0 and l[i-1][j]<101:
            solve(i-1,j,l,ans,"up")
        else:
            solve(i,j+1,l,ans,"right")
class Solution(object):
    def spiralOrder(self, matrix):
        ans=[]
        l=matrix
        solve(0,0,l,ans,"right")
        return ans
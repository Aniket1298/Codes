""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
l=[]
def checkBST(root):
    solve(root)
    flag=1
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            pass
        else:
            flag=0
            break
    return flag
def solve(root):
    if root:
        solve(root.left)
        l.append(root.data)
        solve(root.right)
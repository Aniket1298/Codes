class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.sum=0
def insert(root,node):
    if node.val<root.val:
        if root.left==None:
            root.left=node
        else:
            insert(root.left,node)
    elif node.val>root.val:
        if root.right==None:
            root.right=node
        else:
            insert(root.right,node)
def inorder(root):
    
    if root!=None:
        inorder(root.left)
        print root.val,
        inorder(root.right)
def preorder(root):
    
    if root!=None:
        #print root.val
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        #print(root.val)


def build_bst(l):
    Root=Node(l[0])
    for i in range(1,len(l)):
        insert(Root,Node(l[i]))
    print "Inorder Traversal"
    inorder(Root)
    return Root
Root=build_bst([2,4,1,5,7,9,0,-1,6,10])
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def helper(root, min_val, max_val):
    if root is None or root.left is None or root.right is None: 
        return True
    
    if root.left is not None and root.left.data < root.data and root.left.data < max_val and root.left.data > min_val:
        l_isBST = helper(root.left, min_val, root.data) 
    else:
        l_isBST = False
        
    if root.right is not None and root.right.data > root.data and root.right.data < max_val and root.right.data > min_val:
        r_isBST = helper(root.right, root.data, max_val) 
    else:
        r_isBST = False
        
    if l_isBST and r_isBST :
        return True
    
    return False    

def checkBST(root):
    return helper(root, 0, 10000)



        
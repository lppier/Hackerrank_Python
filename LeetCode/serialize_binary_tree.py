# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        
        alist = []
        queue = []
        queue.append(root)
        # add all the neighbors
        while (queue):
            curr = queue.pop(0)
            if curr is None:
                alist.append('null')
                continue
                
            if curr.left is not None:
                queue.append(curr.left)
            else:
                queue.append(None)
            
            if curr.right is not None:
                queue.append(curr.right)
            else: 
                queue.append(None)
            
            alist.append(str(curr.val))
        alist_str = ','.join(alist)
        return alist_str
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        if len(data) < 0 or data[0]=='':
            return None
            
        root = TreeNode(int(data[0]))
        head = root 
        queue = []
        queue.append(root)
        i = 1
        while queue and i < len(data):
            node = queue.pop(0)
            if data[i] != 'null':
                left = TreeNode(int(data[i]))
                node.left = left
                queue.append(left)
            i += 1
            
            if data[i] != 'null':
                right = TreeNode(int(data[i]))
                node.right= right
                queue.append(right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
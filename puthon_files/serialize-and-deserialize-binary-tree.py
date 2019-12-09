# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

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
        ## if root is none return arbitary values
        if root is None:
            return "S,"
        else:
            left=self.serialize(root.left)
            right=self.serialize(root.right)
        
        return str(root.val)+','+str(left)+str(right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserializeHelper(queue):
            node=queue.popleft()
            if node =='S':
                return None
            
            root=TreeNode(node)
            root.left=deserializeHelper(queue)
            
            root.right=deserializeHelper(queue)
            
            
            return root
        
        
        
        data=data.split(',')
        queue=collections.deque(data)
        
        return deserializeHelper(queue)
        
       
        
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
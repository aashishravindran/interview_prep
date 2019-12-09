# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 814 Pruning Binary Tree
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ## 
        
        def prune_helper(root):
            if root is None:
                return False
              
            left=prune_helper(root.left)
            right=prune_helper(root.right)
            if left==0:
                root.left=None
            if right==0:
                root.right=None
            ## if root has a one or left has a one or right has a one return 
            return root.val or left or right
            
            
        if not root:
            return None 
        prune_helper(root)
        return root
                
         
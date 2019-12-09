# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# /1022. Sum of Root To Leaf Binary Numbers
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node,path):
            if node:
                path+=str(node.val)
                if node.left or node.right:
                    return dfs(node.left,path)+dfs(node.right,path)
                else:
                    return int(path,2)
        
            
            else:                
                return 0
        
        return dfs(root,'')

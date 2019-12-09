# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 236. Lowest Common Ancestor of a Binary Tree
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #Intutution is to first find all parent nodes 
        #Inspired by https://www.youtube.com/watch?v=py3R23aAPCA
        
        def search(root,x,y):
            if root is None:
                return None
            elif root.val == x or root.val == y:
                return root
            left=search(root.left,x,y)
            right=search(root.right,x,y)
            
            if left is None:
                return right
            if right is None:
                return left 
            return root
        
        return search(root,p.val,q.val)
        

      
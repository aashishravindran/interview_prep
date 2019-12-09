# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Lowest Common Ancestor of a Binary Search Tree
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p=p.val
        q=q.val
        queue=root
        while queue:
            parent=queue.val
            if p>parent and q>parent:
                queue=queue.right
            elif p<parent and q<parent:
                queue=queue.left
            else:
                return queue
        
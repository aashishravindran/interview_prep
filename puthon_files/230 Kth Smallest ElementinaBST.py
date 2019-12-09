# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.



# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## Intutiton - InOrder Traversal Of Binary Tree is always sorted
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        arr=[]
        def InOrder(root):
            if not root:
                return 
            InOrder(root.left)
            arr.append(root.val)
            InOrder(root.right)
            
        InOrder(root)
        return arr[k-1]
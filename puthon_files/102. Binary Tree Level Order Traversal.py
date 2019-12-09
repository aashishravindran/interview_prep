

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/binary-tree-level-order-traversal/

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None 
        queue=[root]
        result=[]
        while queue:
            temp=[]
            new_q=[]
            for adjacents in queue:
                temp.append(adjacents.val)
                if adjacents.left:
                    new_q.append(adjacents.left)
                if adjacents.right:
                    new_q.append(adjacents.right)
                
            result.append(temp)
            queue=new_q
        return result 
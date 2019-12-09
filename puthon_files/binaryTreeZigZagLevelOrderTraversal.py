# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        q=[root]
        res=[]
    
        index=0
        while q:
            temp=[]
            new_q=[]
           
            for adjacents in q:
                temp.append(adjacents.val)
                if adjacents.left:
                    new_q.append(adjacents.left)
                if adjacents.right:
                    new_q.append(adjacents.right)
            if index%2==0:
                res.append(temp)
            else:
                res.append(temp[::-1])
            q=new_q
            
            index+=1
        return res
                    
                
                    
       
        
        
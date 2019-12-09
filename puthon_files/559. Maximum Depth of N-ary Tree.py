# 559. Maximum Depth of N-ary Tree
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        stack=[]
        if  root is not None:
            stack.append((1,root))
            
        depth=0
        while stack:
            curr,node=stack.pop()
            if node is not None:
                depth=max(depth,curr)
                for children in node.children:
                    stack.append((curr+1,children))
        return depth 

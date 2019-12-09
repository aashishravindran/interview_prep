# 257. Binary Tree Paths
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        arr=[]
        
        def binary_tree_helper(root,path=None):
            if path is None:
                path=''
            if root:
                path+=str(root.val)
                
                if root.left is not None or root.right is not  None:
                    path += '->'
                    binary_tree_helper(root.left,path)
                    binary_tree_helper(root.right,path)
                else:
                    arr.append(path)
                    
            else:
                
                return arr
        
        binary_tree_helper(root)        
        return arr
        
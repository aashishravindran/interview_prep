class TreeNode:
	def __init__(self,node):
		self.left=None
		self.right=None
		self.val=node

	

	def InOrder(self,root):
		 # Traverse left sub Tree 
		 # visit Root 
		 # Traverese Right Sub Tree
		if root is None:
			return 
		else:
	    		self.InOrder(root.left) # do in order of left child
    			print(root.val)  # print root of the given tree
    			self.InOrder(root.right)


	def preOrder(self,root):
		# Visit the root.
  		#Taverse the left subtree, i.e., call Preorder(left-subtree)
  		#Traverse the right subtree, i.e., call Preorder(right-subtree) 
  		if root is None:
  			return 
  		print(root.val)
  		self.preOrder(root.left)
  		self.preOrder(root.right)

  	def postOrder(self,root):
  		if root is None:
  			return 
  		self.postOrder(root.left)
  		self.postOrder(root.right)
  		print(root.val)


root = TreeNode(1) 
root.left= TreeNode(2) 
root.right = TreeNode(3) 
root.left.left= TreeNode(4) 
root.left.right= TreeNode(5) 

# root.InOrder(root)
# root.preOrder(root)
root.postOrder(root)


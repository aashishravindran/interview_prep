class Node:
	"""docstring for Node"""
	def __init__(self, val=None):
		self.val=val
		self.next=None 
class LinkedList:
	def __init__(self):
		self.head=Node()
	
	def insert (self,data):
		# iterate through all the elements in the list and insert at the end
		new_node=Node(data)
		curr=self.head
		while curr.next!= None:
			 curr=curr.next
		curr.next=new_node

	def traverse_linked_list(self):
		curr_node=self.head
		while curr_node.next is not None:
			curr_node=curr_node.next
			print(curr_node.val)

	def rightshift(self,k):
			if not self.head:
				return None
			tail=self.head
			size=1
			while tail.next is not None:
				tail=tail.next
				size+=1
		
			tail.next=self.head.next

			
			new_tail_loc=size-k
			rotated_tail=Node()
			rotated_tail.next=tail
			while new_tail_loc>0:
				rotated_tail=rotated_tail.next
				new_tail_loc-=1

			new_head=Node()
			new_head.next=rotated_tail.next
			rotated_tail.next=None
			self.head=new_head
			
			
			


linked=LinkedList()
linked.insert(21)
linked.insert(22)
linked.insert(23)
linked.insert(24)
 

print("--s")
#21->22->23->24
##24->21->22->23
linked.rightshift(1)
linked.traverse_linked_list()
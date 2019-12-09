class Node:
	"""docstring for Node"""
	def __init__(self, val=None):
		self.val=val
		self.next=None 
##Node class creates a Node
##Wrapper Class for Linked List

class LinkedList:
	def __init__(self):
		self.head=Node()
		print(self.head.val)

	def insert (self,data):
		# iterate through all the elements in the list and insert at the end
		new_node=Node(data)
		curr=self.head
		while curr.next!= None:
			 curr=curr.next
		curr.next=new_node

	def insert_at_nth_position(self,index,data):
		new_node=Node(data)

		curr_node =self.head
		curr_index=0
		if index>=self.get_length():
			return "Eror"

		while curr_node.next!= None:
			last_node=curr_node
			curr_node=curr_node.next
			if index==curr_index:
				last_node.next=new_node
				new_node.next=curr_node

			curr_index+=1


	def get_length(self):
		curr=self.head
		count=0
		while curr.next is not None:
			curr=curr.next
			count+=1
		return count


	def traverse_linked_list(self):
		curr_node=self.head
		while curr_node.next is not None:
			curr_node=curr_node.next
			print(curr_node.val)

	def remove_from_index(self,index):
		if index>=self.get_length():
			return "Erroor"
		curr_node=self.head
		curr_index=0
		while True:
			last_node=curr_node
			curr_node=curr_node.next
			if curr_index==index:
				last_node.next=curr_node.next
				return

			curr_index+=1


	def reverse(self):
		curr=self.head
		prev=None
		while curr is not  None:
			nextval=curr.next
			curr.next=prev 
			prev=curr
			curr=nextval
		self.head=prev



linked=LinkedList()
linked.insert(21)
linked.insert(22)
linked.insert(23)
linked.insert(24)



print("--s")
linked.reverse()
linked.traverse_linked_list()
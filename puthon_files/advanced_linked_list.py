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
	
	

	def insert (self,data):
		# iterate through all the elements in the list and insert at the end
		new_node=Node(data)
		curr=self.head
		while curr.next!= None:
			 curr=curr.next
		curr.next=new_node

	

	def reverse(self):
		curr=self.head
		prev=None
		while curr is not  None:
			nextval=curr.next
			curr.next=prev 
			prev=curr
			curr=nextval
		self.head=prev

	def traverse_linked_list(self):
		curr_node=self.head
		while curr_node.next is not None:
			print(curr_node.val)
			curr_node=curr_node.next
	
linked=LinkedList()
linked.insert(21)
linked.insert(22)
linked.insert(23)
linked.insert(24)
 

print("--s")
#21->22->23->24
##24->21->22->23
linked.rightshift(2)
linked.traverse_linked_list()

# Copying a list with a random pointer
# class Solution(object):
#     def copyRandomList(self, head):
#         """
#         :type head: Node
#         :rtype: Node
#         """
#         cloneMap={}
#         curr=head
#         while curr is not None:
#             cloneMap[curr]=ListNode(curr.val)
#             curr=curr.next
#         curr=head
#         while curr is not None:
#             cloneMap.get(curr).next=cloneMap.get(curr.next)
#             cloneMap.get(curr).random=cloneMap.get(curr.random)
#             curr=curr.next
#         return cloneMap.get(head)
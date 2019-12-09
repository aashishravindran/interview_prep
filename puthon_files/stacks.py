class stack:
	
	def __init__(self):
		self.arr=[]
		self.top=-1
	
	def push(self,data):
		self.top+=1
		self.arr.append(data)
	
	def print_val(self):
		print(self.arr)
	
	def pop(self):
		self.arr.pop()
		self.top-=1

	def is_Empyty(self):
		if self.top == -1:
			return False
		else:
			return True
			 
	def top_val(self):
		return self.arr[self.top]



stack= stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.print_val()

stack.pop()

stack.print_val()

print(stack.is_Empyty())
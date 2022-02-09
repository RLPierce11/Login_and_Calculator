#stack class for calculator

class Stack:
	def __init__(self):
		self.arr = []
		self.mysize = 0
		self.mytop = self.mysize - 1

	def size(self):
		return self.mysize

	def empty(self):
		if(self.mysize == 0):
			return True
		else:
			return False

	def top(self):
		if(not self.empty()):
			return self.arr[self.mytop]
		else:
			print("Stack is Empty!")
			return

	def push(self, value):
		self.arr.append(value)
		self.mysize += 1
		self.mytop += 1

	def pop(self):
		self.arr.pop()
		self.mysize -= 1
		self.mytop -= 1





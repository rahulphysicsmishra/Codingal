class GFG:
	# Node of a doubly linked list
	class Node:
		data = 0
		prev = None
		next = None

		# Function to get a new node
		@staticmethod
		def getnode(data):
			newNode = GFG.Node()
			newNode.data = data
			newNode.prev = None
			newNode.next = None
			return newNode

	# A structure to represent a deque
	class Deque:
		front = None
		rear = None
		Size = 0

		def __init__(self):
			self.front = None
			self.rear = None
			self.Size = 0

		# Function to check whether deque
		# is empty or not
		def isEmpty(self):
			return (self.front == None)

		# Function to return the number of
		# elements in the deque
		def size(self):
			return self.Size

		# Function to insert an element
		# at the front end
		def insertFront(self, data):
			newNode = GFG.Node.getnode(data)

			# If true then new element cannot be added
			# and it is an 'Overflow' condition
			if (newNode == None):
				print("OverFlow\n", end="")
			else:

				# If deque is empty
				if (self.front == None):
					self.rear = newNode
					self.front = newNode
				else:
					newNode.next = self.front
					self.front.prev = newNode
					self.front = newNode

				# Increments count of elements by 1
				self.Size += 1

		# Function to insert an element
		# at the rear end
		def insertRear(self, data):
			newNode = GFG.Node.getnode(data)

			# If true then new element cannot be added
			# and it is an 'Overflow' condition
			if (newNode == None):
				print("OverFlow\n", end="")
			else:

				# If deque is empty
				if (self.rear == None):
					self.front = newNode
					self.rear = newNode
				else:
					newNode.prev = self.rear
					self.rear.next = newNode
					self.rear = newNode
				self.Size += 1

		# Function to delete the element
		# from the front end
		def deleteFront(self):

			# If deque is empty then
			# 'Underflow' condition
			if (self.isEmpty()):
				print("UnderFlow\n", end="")
			else:
				temp = self.front
				self.front = self.front.next

				# If only one element was present
				if (self.front == None):
					self.rear = None
				else:
					self.front.prev = None

				# Decrements count of elements by 1
				self.Size -= 1

		# Function to delete the element
		# from the rear end
		def deleteRear(self):

			# If deque is empty then
			# 'Underflow' condition
			if (self.isEmpty()):
				print("UnderFlow\n", end="")
			else:
				temp = self.rear
				self.rear = self.rear.prev

				# If only one element was present
				if (self.rear == None):
					self.front = None
				else:
					self.rear.next = None

				# Decrements count of elements by 1
				self.Size -= 1

		# Function to return the element
		# at the front end
		def getFront(self):

			# If deque is empty, then returns
			# garbage value
			if (self.isEmpty()):
				return -1
			return self.front.data

		# Function to return the element
		# at the rear end
		def getRear(self):

			# If deque is empty, then returns
			# garbage value
			if (self.isEmpty()):
				return -1
			return self.rear.data

		# Function to delete all the elements
		# from Deque
		def erase(self):
			self.rear = None
			while (self.front != None):
				temp = self.front
				self.front = self.front.next
			self.Size = 0

	# Driver program to test above
	@staticmethod
	def main(args):
		dq = GFG.Deque()
		print("Insert element \'5\' at rear end\n", end="")
		dq.insertRear(5)
		print("Insert element \'10\' at rear end\n", end="")
		dq.insertRear(10)
		print("Rear end element: " + str(dq.getRear()) + "\n", end="")
		dq.deleteRear()
		print("After deleting rear element new rear" +
			" is: " + str(dq.getRear()) + "\n", end="")
		print("Inserting element \'15\' at front end \n", end="")
		dq.insertFront(15)
		print("Front end element: " + str(dq.getFront()) + "\n", end="")
		print("Number of elements in Deque: " + str(dq.size()) + "\n", end="")
		dq.deleteFront()
		print("After deleting front element new " +
			"front is: " + str(dq.getFront()) + "\n", end="")


if __name__ == "__main__":
	GFG.main([])
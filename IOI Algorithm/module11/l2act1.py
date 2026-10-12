class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        return True if self.head == None else False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def topElement(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def pop(self):
        if self.isempty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None

            return popped_node.data

# Driver code
stack_obj = Stack()
stack_obj.push(5)
stack_obj.push(2)
stack_obj.push(7)
stack_obj.push(8)
print("the element at the top")
print(stack_obj.topElement())
print("the element popped")
print(stack_obj.pop())
print("the element at the top")
print(stack_obj.topElement())
print("the element popped")

print("the element at the top")
print(stack_obj.topElement())
print("the element popped")
print(stack_obj.pop())
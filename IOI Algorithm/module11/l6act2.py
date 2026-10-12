from collections import deque

class Stack:
    def __init__(self):
        # Two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        # if no elements are there in q1
        if (not self.q1):
            return
        # Leave one element in q1 and push others in q2
        while(len(self.q1) != 1):
            self.q2.append(self.q1.popleft())

        # Swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

    def top(self):
        # if no elements are there in q1
        if (not self.q1):
            return
        # Leave one element in q1 and push others in q2
        while(len(self.q1) != 1):
            self.q2.append(self.q1.popleft())

        # Pop the only left element from q1 to q2
        top = self.q1[0]
        self.q2.append(self.q1.popleft())

        # Swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

        return top

    def size(self):
        return len(self.q1)

# Driver Code
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print("Current size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())

    print("Current size: ", s.size())
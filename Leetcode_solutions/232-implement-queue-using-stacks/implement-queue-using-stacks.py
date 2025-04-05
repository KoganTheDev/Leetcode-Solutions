class Stack:
    """
    A simple Stack implementation (LIFO - Last In, First Out)
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class MyQueue:
    """
    Queue implementation using two stacks
    """

    def __init__(self):
        self.stack1 = Stack()  # Input stack
        self.stack2 = Stack()  # Output stack

    def push(self, x):
        self.stack1.push(x)

    def pop(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

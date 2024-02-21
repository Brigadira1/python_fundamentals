from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def is_empty(self):
        return len(self.stack) == 0

    def get_stack(self):
        deque = []

        if self.is_empty():
            print("Stack is empty")
            return

        for item in self.stack:
            deque.append(item)

        return deque

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack is empty - nothing to pop.")
            return

        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty - nothing to peek.")
            return

        return self.stack[-1]


stack = Stack()
print(stack.is_empty())
stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")
print(stack.get_stack())
stack.pop()
print(stack.get_stack())
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.get_stack())

print(stack.is_empty())
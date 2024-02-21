class ListStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        if self.is_empty():
            print("Stack is empty.")
            return

        return self.items

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack is empty - nothing to pop.")
            return

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty - nothing to peek.")
            return

        return self.items[-1]


stack = ListStack()
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

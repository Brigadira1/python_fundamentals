from typing import Any


class Stack:

    def __init__(self) -> None:
        self._stack: list[Any] = []

    def is_empty(self) -> bool:
        return self._stack == []

    def push(self, data: Any) -> None:
        self._stack.append(data)
        print(f"{data} was added in the stack.")

    def pop(self) -> Any:
        if not self.is_empty():
            return self._stack.pop()
        else:
            print("The stack is empty. Nothing to pop.")

    def __str__(self) -> str:
        reversed_list = self._stack.copy()
        reversed_list.reverse()
        r_list = [str(data) for data in reversed_list]
        return "\n".join(r_list)

    def peek(self) -> Any:
        if self.is_empty():
            print("The list is empty.")
        else:
            return self._stack[-1]

    def delete_stack(self) -> None:
        self._stack = []


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(f"The peek of the stack is {stack.peek()}.")
    print(stack)
    print(f"Poping the last element of the stack {stack.pop()}")
    print(f"The peek of the stack is {stack.peek()}.")
    print(stack)

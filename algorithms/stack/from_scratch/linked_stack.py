from typing import Any

from .linked_list import LinkedList
from .node import Node


class LinkedStack:

    def __init__(self) -> None:

        self._linked_list = LinkedList()

    def is_empty(self) -> bool:

        return self._linked_list.head is None

    def push(self, data: Any) -> Any:

        node = Node(data)
        node.next = self._linked_list.head
        self._linked_list.head = node
        data = self._linked_list.head.data
        return data

    def pop(self) -> Any:

        data = self._linked_list.head.data
        self._linked_list.head = self._linked_list.head.next
        return data

    def peek(self) -> Any:

        data = self._linked_list.head.data
        return data

    def print(self) -> None:
        if self.is_empty():
            print("The stack is empty - nothing to print")
            return
        stack_elements = []
        pointer = self._linked_list.head
        while pointer:
            stack_elements.append(pointer.data)
            pointer = pointer.next
        print(f"All elements of the stack are: {stack_elements}")

    def delete_stack(self) -> None:
        self._linked_list.head = None


if __name__ == "__main__":
    l_stack = LinkedStack()

    print(f"Is the stack empty: {l_stack.is_empty()}")
    print(l_stack.push(1))
    print(l_stack.push(2))
    print(l_stack.push(3))
    print(l_stack.push(4))
    print(l_stack.push(5))
    print(f"The peek of the stack is: {l_stack.peek()}")
    l_stack.print()

    print(l_stack.pop())
    print(l_stack.pop())
    print(l_stack.pop())
    print(f"The peek of the stack is: {l_stack.peek()}")
    l_stack.print()
    l_stack.delete_stack()
    l_stack.print()

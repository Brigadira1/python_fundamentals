from typing import Any

from .Node import Node


class SinglyLinkedList:

    def __init__(self) -> None:

        self._head: Node | None = None
        self._tail: Node | None = None

    def is_empty(self) -> bool:

        if self._head:
            return False
        return True

    def __iter__(self):

        current_node = self._head

        while current_node:
            yield current_node
            current_node = current_node.next

    def print(self):

        all_elements: list[Any] = [str(node.data) for node in self]
        all_elements_as_string = " --> ".join(all_elements)
        print(all_elements_as_string)

    def show_head(self) -> Any:
        if self.is_empty():
            return None

        return self._head.data

    def show_tail(self) -> Any:
        if self.is_empty():
            return None

        return self._tail.data

    def insert_at_beginning(self, data: Any) -> None:

        new_node = Node(data)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node

    def insert_at_end(self, data: Any) -> None:

        new_node = Node(data)
        self._tail.next = new_node
        new_node.next = None
        self._tail = new_node

    def insert_at_index(self, data: Any, index: int) -> None:

        if self.is_empty() or index == 0:
            self.insert_at_beginning(data)
        else:
            new_node = Node(data)
            pointer = self._head
            current_index = 0
            while current_index < index - 1:
                pointer = pointer.next
                current_index += 1

            """This is necessary to move the tail to the last element. 
               If these two lines of code are ommited the tail doesn't move if the index is after the last current index """
            if pointer == self._tail:
                self.insert_at_end(data)
            else:
                new_node.next = pointer.next
                pointer.next = new_node

    def delete_at_beginning(self) -> None:

        if self.is_empty():
            print("The Linked List is empty. Nothing to delete")
            return

        print(
            f"Element with {self._head.data} data was deleted from the beginning of the list"
        )
        self._head = self._head.next

    def delete_at_index(self, index: int) -> None:

        if self.is_empty():
            print("The Linked List is empty. Nothing to delete.")
            return

        if index == 0:
            self.delete_at_beginning()
            return

        pointer = self._head
        current_index = 0
        while current_index < index - 1:
            pointer = pointer.next
            current_index += 1

        if pointer.next == self._tail:
            self._tail = pointer
            pointer.next = None
            return

        pointer.next = pointer.next.next


if __name__ == "__main__":
    s_list = SinglyLinkedList()
    s_list.insert_at_beginning(1)
    s_list.insert_at_beginning(2)
    s_list.insert_at_beginning("BEGINNING")
    s_list.insert_at_end("END")
    s_list.print()
    s_list.insert_at_index("After END", 4)
    s_list.print()
    s_list.insert_at_index("AFTER After END", 5)
    s_list.print()
    s_list.delete_at_beginning()
    s_list.print()
    print()
    s_list.delete_at_index(4)
    s_list.print()
    s_list.delete_at_index(2)
    s_list.print()
    print(f"Head value is {s_list.show_head()} and Tail value is {s_list.show_tail()}")

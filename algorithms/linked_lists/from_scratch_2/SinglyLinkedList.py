from typing import Any

from .Node import Node


class SinglyLinkedList:
    def __init__(self, head: Node | None = None) -> None:
        self._head = head
        self._size = 0

    def getsize(self) -> int:
        return self._size

    def is_empty(self):
        if self.getsize():
            return False
        return True

    def print(self) -> None:

        if self.is_empty():
            print("The linked list is empty")
        else:
            pointer = self._head
            print_list = ""

            while pointer:
                data = pointer.data
                print_list += f"{data} --> "
                pointer = pointer.next

            print(print_list)
            print(f"The data in the head is {self._head.data}")
            print()

    def add_at_beginning(self, data) -> None:
        node = Node(data)
        node.next = self._head
        self._head = node
        self._size += 1

        print(f"{node.data} is added at the beginning of the linked list")

    def add_at_end(self, data) -> None:
        node = Node(data)
        if self.is_empty():
            self._head = node
        pointer = self._head
        while pointer:
            if pointer.next:
                pointer = pointer.next

            else:
                pointer.next = node
                break

        print(f"{node.data} is added at the END of the link list")

    def add_at_index(self, index: int, data: Any) -> None:
        if not index:
            self.add_at_beginning(data)
            print(
                f"As the index is {index} the element was added at the beginning of the list"
            )
        elif index == self.getsize():
            self.add_at_end(data)
            print(
                f"As the index is {index} and the size of the list is {self.getsize()} the element was added at the END of the list as the last element"
            )
        else:
            self._size += 1
            pointer = self._head
            current_index = 0
            while current_index + 1 != index:
                pointer = pointer.next
                current_index += 1
            node = Node(data)
            node.next = pointer.next
            pointer.next = node
            print(f"The element was added after {current_index}")

    def delete_by_data(self, data: Any) -> None:
        found = False
        pointer: Node | None = self._head
        if self.is_empty():
            print("The linked list is empty. Nothing to remove.")
        else:
            if self.getsize() == 1 and pointer.data == data:
                self._head = None
                self._size = 0
                found = True
            else:
                while pointer.next:
                    if pointer.next.data == data:
                        found = True
                        pointer.next = pointer.next.next
                        self._size -= 1
                        break
                    pointer = pointer.next

            if found:
                print(f"Element with data: {data} was deleted from the list")
                self._size -= 1
            else:
                print(
                    f"Element with data: {data} was NOT FOUND in the list and therefore cannot be deleted"
                )

    def delete_by_index(self, index: int) -> None:

        if index < 0 or index + 1 > self.getsize():
            print("Index out of range!!!")
            return
        if self.is_empty():
            print("The list is empty - nothing to delete")
        else:
            if self.getsize() == 1 and index == 0:
                self._head = None
                print("Only 1 element detected in the list and it was deleted.")
                self._size = 0
            else:
                pointer = self._head
                current_index = 0

                if current_index == index:
                    self._head = pointer.next
                    self._size -= 1

                while current_index + 1 < index:
                    pointer = pointer.next
                    current_index += 1

                pointer.next = pointer.next.next
                print(f"Element at index {index} was deleted from the list")


if __name__ == "__main__":
    l_list = SinglyLinkedList()
    # print(l_list.getsize())
    # print(l_list.is_empty())

    l_list.add_at_beginning(1)
    l_list.print()

    l_list.add_at_beginning(2)
    l_list.print()

    l_list.add_at_beginning(3)
    l_list.print()

    l_list.add_at_beginning(4)
    l_list.print()

    l_list.add_at_beginning(5)
    l_list.print()

    l_list.add_at_end(6)
    l_list.print()

    l_list.add_at_end(7)
    l_list.print()

    l_list.add_at_end(8)
    l_list.print()

    l_list.add_at_end(999)
    l_list.print()

    l_list.add_at_index(0, "Beginning")
    l_list.print()

    l_list.add_at_index(10, "END")
    l_list.print()

    l_list.add_at_index(1, "First Index")
    l_list.print()

    l_list.add_at_index(2, "Second Index")
    l_list.print()

    l_list.delete_by_data("Second Index")
    l_list.print()

    l_list.delete_by_data("END")
    l_list.print()
    # l_list.delete_by_index(0)
    # l_list.print()

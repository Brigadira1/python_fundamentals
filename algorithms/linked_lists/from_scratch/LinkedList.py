from .Node import Node

# from algorithms.linked_lists.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def is_list_empty(self):
        return self.head is None

    def is_single_element(self):
        if self.is_list_empty():
            return False

        return self.head.next is None

    def print_all_elements(self):
        current_node = self.head
        all_elements = []

        if self.is_list_empty():
            return all_elements

        while current_node is not None:
            node_data = current_node.data
            all_elements.append(node_data)
            current_node = current_node.next

        return all_elements

    def length(self):
        if self.is_list_empty():
            return 0

        current_node = self.head
        number_of_elements = 0

        while current_node is not None:
            number_of_elements += 1
            current_node = current_node.next

        return number_of_elements

    def add_at_the_end(self, data):
        new_node = Node(data)

        if self.is_list_empty():
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def add_in_the_beginning(self, data):
        new_node = Node(data)

        if self.is_list_empty():
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def add_after(self, previous_node, data):

        if previous_node is None:
            print("Previous node must exists in order to put data after it!")
            return

        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def delete_by_index(self, index):
        if self.is_list_empty() or index >= self.length():
            return -1

        if index == 0 and self.is_single_element():
            self.head = None
            return index
        elif index == 0:
            self.head = self.head.next
            return index

        if index == self.length() - 1:
            current_before_last = self.head
            while current_before_last.next.next is not None:
                current_before_last = current_before_last.next
            current_before_last.next = None
            return index

        previous_node = self.head
        current_node = previous_node.next
        node_index = 1

        while previous_node.next.next is not None:
            if index == node_index:
                previous_node.next = current_node.next
                return index
            previous_node = current_node
            current_node = current_node.next
            node_index += 1

        return -1

    def delete_by_data(self, data):
        if self.is_list_empty():
            print("Nothing to delete - the list is empty!")
            return

        if self.is_single_element():
            if self.head.data == data:
                self.head = None
                return

        current_node = self.head
        previous_node = current_node

        if current_node.data == data:
            self.head = current_node.next
            return
        current_node = current_node.next

        while current_node is not None:
            if current_node.data == data:
                previous_node.next = current_node.next
                return

            previous_node = current_node
            current_node = current_node.next

    def search_by_data(self, data):
        current_node = self.head
        element_index = 0

        if self.is_list_empty():
            return -1

        while current_node is not None:
            if current_node.data == data:
                return element_index
            element_index += 1
            current_node = current_node.next

        return -1


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.add_in_the_beginning(108)
    linked_list.add_at_the_end(1)
    linked_list.add_at_the_end(2)
    linked_list.add_at_the_end(3)
    linked_list.add_at_the_end(4)
    linked_list.add_at_the_end(5)
    linked_list.add_at_the_end(6)
    linked_list.add_at_the_end(7)
    linked_list.add_at_the_end(98)

    print(linked_list.delete_by_index(0))
    linked_list.delete_by_data(3)
    linked_list.delete_by_data(98)
    linked_list.delete_by_data(1)
    linked_list.delete_by_data(2)

    linked_list.delete_by_data(4)
    linked_list.delete_by_data(5)
    linked_list.delete_by_data(6)
    linked_list.delete_by_data(7)
    linked_list.delete_by_data(3)
    print(linked_list.print_all_elements())

    # print(linked_list.length())
    # print(linked_list.search_by_data(7))

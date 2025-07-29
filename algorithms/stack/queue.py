from typing import Any


class Queue:

    def __init__(self) -> None:
        self._queue = []

    def is_empty(self) -> bool:
        return self._queue == []

    def enqueue(self, data: Any) -> None:
        self._queue.append(data)

    def dequeue(self) -> None:
        self._queue.pop(0)

    def peek(self) -> Any:
        if self.is_empty():
            print("The queue is empty")
            return
        return self._queue[0]

    def delete_queue(self) -> None:
        self._queue = []

    def print_queue(self) -> None:
        if self.is_empty():
            print("The queue is empty - nothing to print.")
            return
        queue = [str(element) for element in self._queue]
        print(queue)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(f"The first element in the queue is: {queue.peek()}")
    queue.print_queue()

    queue.dequeue()
    queue.enqueue(100)
    queue.dequeue()
    queue.dequeue()
    queue.print_queue()
    print(f"The first element in the queue is: {queue.peek()}")
    queue.dequeue()
    queue.dequeue()
    queue.delete_queue()
    queue.print_queue()

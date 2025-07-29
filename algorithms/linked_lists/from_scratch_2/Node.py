from typing import Any


class Node:
    def __init__(self, data: Any | None = None, next: Any | None = None) -> None:
        self.data: Any | None = data
        self.next: Any = next

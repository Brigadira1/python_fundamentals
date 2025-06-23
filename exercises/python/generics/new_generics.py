type IntOrSet = int | set

type ListOrSet[T] = list[T] | set[T]


class Box[T]:
    def __init__(self, item: T):
        self.item = item

    def get_item(self) -> T:
        return self.item

    def set_item(self, item: T) -> None:
        self.item = item


def get_first_item[T](items: list[T]) -> T:
    return items[0]


def main() -> None:
    int_box = Box(124)
    int_item = int_box.get_item()
    print(type(int_box))
    print(int_item)

    str_box = Box("Hello Generics")
    str_item = str_box.get_item()
    print(str_item)

    list_box = Box([1, 2, 3])
    list_item = list_box.get_item()
    print(list_item)

    first_item = get_first_item([1, 2, 3])
    print(first_item)


if __name__ == "__main__":
    main()

def bubble_sort(unsorted_list: list[int]) -> None:
    n: int = len(unsorted_list)
    for i in range(n):
        sorted: bool = False
        for j in range(n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = (
                    unsorted_list[j + 1],
                    unsorted_list[j],
                )
                sorted = True
        if not sorted:
            break


list = [1, 120, 111, 4, 4, 5, 6, 3, 2]
bubble_sort(list)
print(list)

import time


def calc_square(numbers):
    result = []
    start = time.time()
    for number in numbers:
        result.append(number * number)
    end = time.time()
    print("calc_squares took " + str((end - start) * 1000) + " mil seconds")
    return result


def calc_cube(numbers):
    result = []
    start = time.time()
    for number in numbers:
        result.append(number * number * number)
    end = time.time()
    print("calc_cubes took " + str((end - start) * 1000) + " mil seconds")
    return result


array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)

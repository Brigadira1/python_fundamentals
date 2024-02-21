def A(num):
    if num > 0:
        # print(num)
        A(num - 1)
        print(num)

num = 3
A(num)
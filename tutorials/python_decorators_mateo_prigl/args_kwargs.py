def test_function(*args, **kwargs):
    print(*args)
    print(*kwargs)
    print(
        f"Printing all the arguments: Positional arguments: {args}\n Keyword arguments: {kwargs}"
    )


test_function(
    1,
    2,
    3,
    "shit",
    [1, 2, 3, 4, 5],
    key=2,
    open="I am open key word argument",
    lister=[1, 2, 3, 1000000],
)

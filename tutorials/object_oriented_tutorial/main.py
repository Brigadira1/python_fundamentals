from item import Item


def main():
    Item.instantiate_from_csv()
    print(Item.all)


if __name__ == "__main__":
    main()

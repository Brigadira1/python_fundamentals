from pathlib import Path

import pandas as pd

base_dir: Path = Path(__file__).resolve().parent
squirrel: Path = (
    base_dir / "./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250630.csv"
)
squirrel_count: Path = base_dir / "squirrel_count.csv"

data = pd.read_csv(squirrel)

different_colors = set(data["Primary Fur Color"])
print(different_colors)

gray_fur_data = data[data["Primary Fur Color"] == "Gray"]
black_fur_data = data[data["Primary Fur Color"] == "Black"]
cinnamon_fur_data = data[data["Primary Fur Color"] == "Cinnamon"]

gray_fur_number = len(gray_fur_data["Primary Fur Color"].to_list())
black_fur_number = len(black_fur_data["Primary Fur Color"].to_list())
cinnamon_fur_number = len(cinnamon_fur_data["Primary Fur Color"].to_list())

print(
    f"Gray fur: {gray_fur_number}, Black fur: {black_fur_number}, Cinnamon fur: {cinnamon_fur_number}"
)

fur_numbers_data = pd.DataFrame(
    {
        "Fur Color": ["gray", "red", "black"],
        "Count": [gray_fur_number, black_fur_number, cinnamon_fur_number],
    }
)

fur_numbers_data.to_csv(squirrel_count)

# print(data)
# print(data)
# print(data[data.day == "Monday"])
# print(data.temp)
# temp_list: Series = data.temp
# print(f"The average temperature for the week is: {data.temp.mean()}")
# print(f"The maximum temperature during the week is {data.temp.max()}")
#
# print(
#     f"The row with data, where the temperature is at the maximum is {data[data.temp == data.temp.max()]}"
# )


# fur_color_gray = data[data["Primary Fur Color"] == "Gray"]
# fur_color_white = data[data["Primary Fur Color"] == "White"]
# fur_color_black = data[data["Primary Fur Color"] == "Black"]
#
# print(f"The number of black squirrels is: {fur_color_black.size}")
# print(f"The number of white squirrels is: {fur_color_white.size}")
# print(f"The number of gray squirrels is: {fur_color_gray.size}")

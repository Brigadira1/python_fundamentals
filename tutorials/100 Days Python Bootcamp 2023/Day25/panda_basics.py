from pathlib import Path

import pandas as pd

base_dir: Path = Path(__file__).resolve().parent
squirrel: Path = (
    base_dir / "./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250630.csv"
)

data = pd.read_csv(squirrel)

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

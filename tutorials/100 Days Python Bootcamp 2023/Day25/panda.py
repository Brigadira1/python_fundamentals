import csv
from pathlib import Path


def main() -> None:
    current_dir: Path = Path(__file__).resolve().parent
    weather_data: Path = current_dir / "weather_data.csv"

    with weather_data.open("r", encoding="utf-8") as wd_file:

        temperatures = []

        data = csv.reader(wd_file)
        next(data)

        for row in data:
            temp = row[1]
            temperatures.append(int(temp))
            print(f"Appended: {temp}")

        print(temperatures)


if __name__ == "__main__":
    main()

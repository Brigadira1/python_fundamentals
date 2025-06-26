from pathlib import Path

import pandas as pd

base_dir: Path = Path(__file__).resolve().parent
weather_path: Path = base_dir / "weather_data.csv"

data = pd.read_csv(weather_path)
# print(data)
print(data["temp"])

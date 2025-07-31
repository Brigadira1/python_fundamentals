import requests
import json
from pathlib import Path

current_dir = Path(__file__).resolve().parent
print(current_dir)
json_file = current_dir / "test_json.json"

request = requests.get("https://jsonplaceholder.typicode.com/posts/1")
with json_file.open("w") as fp:
    json.dump(request.json(), fp)

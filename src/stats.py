import json


def load_stats(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)["stats"]

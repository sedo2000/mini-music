import json
from pathlib import Path

DB_FILE = Path("data/tracks.json")


def load_tracks():
    if not DB_FILE.exists():
        return []
    return json.loads(DB_FILE.read_text())


def save_tracks(data):
    DB_FILE.write_text(json.dumps(data, indent=2))

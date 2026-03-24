from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent.parent / "MidoGhanamBot"

def getBaseURL():
    with open(BASE_DIR / "main.json", "r") as f: data = json.load(f)
    return data["BASE_URL"]

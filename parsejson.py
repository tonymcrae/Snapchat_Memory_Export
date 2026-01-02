import json
import os
import requests
from pathlib import Path

#Define variables
JSON_PATH = Path("memories_history.json")
ITEMS_KEY = "Saved Media"
PARSE_LIMIT = 20

def main():
    file = JSON_PATH.open("r", encoding="utf-8")
    data = json.load(file)
    file.close()

    items = data[ITEMS_KEY]
    print("Item count:", len(items))
    
    print("\n--- Inspecting items (limited) ---")
    count = 0
    for item in items:
        print(f"\n=== Inspecting item {count} ===")
        print("Keys/value:")
        for key in item:
            value = item[key]
            print(" -", key, ":", value)
        count += 1
        if count >= PARSE_LIMIT:
            break
main()

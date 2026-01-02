import json
import os
import requests
from pathlib import Path

### Config ###
JSON_PATH = Path("memories_history.json")
ITEMS_KEY = "Saved Media"
DOWNLOAD_FOLDER = Path("downloads")
MEDIA_URL_KEY = "Media Download Url"
TIMESTAMP_KEY = "Date"
MEDIA_TYPE_KEY = "Media Type"

def download_media(item):
    media_url = item.get(MEDIA_URL_KEY)
    timestamp = item.get(TIMESTAMP_KEY)
    media_type = item.get(MEDIA_TYPE_KEY)
    safe_timestamp = timestamp.replace(":", "-").replace(" ", "_")

    if media_type == "Image":
        type = "image"
        ext = ".jpg"
    elif media_type == "Video":
        type = "video"
        ext = ".mp4"
    else:
        type = "fixme"
        ext = ".fixme"

    filename = f"{safe_timestamp}_{type}{ext}"
    output_path = DOWNLOAD_FOLDER / filename

    print(f"Downloading media from to {output_path}")
    response = requests.get(media_url)
    print("HTTP status:", response.status_code)
    output_path.write_bytes(response.content)



def main():
    file = JSON_PATH.open("r", encoding="utf-8")
    data = json.load(file)
    file.close()
    items = data[ITEMS_KEY]
    count = 0
    for item in items:
        download_media(item)
        count += 1
main()

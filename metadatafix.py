from datetime import datetime, timezone

# Example filename from your downloads folder
filename = "2026-01-01_17-19-53_UTC_image.jpg"

# 1) Remove extension
name_no_ext = filename.rsplit(".", 1)[0]

# 2) Split filename parts
# Expected: date_time_timezone_type
parts = name_no_ext.split("_")

date_part = parts[0]       # 2026-01-01
time_part = parts[1]       # 17-19-53
timezone_part = parts[2]   # UTC

print("Date part:", date_part)
print("Time part:", time_part)
print("Timezone:", timezone_part)

# 3) Convert time to HH:MM:SS
time_part = time_part.replace("-", ":")

# 4) Build datetime string
# 2026-01-01 17:19:53
dt_text = f"{date_part} {time_part}"
print("Datetime text:", dt_text)

# 5) Parse into datetime (assume UTC)
dt = datetime.strptime(dt_text, "%Y-%m-%d %H:%M:%S")
dt = dt.replace(tzinfo=timezone.utc)

print("Parsed datetime:", dt)

# 6) Convert to EXIF format
exif_text = dt.strftime("%Y:%m:%d %H:%M:%S")
print("EXIF DateTimeOriginal would be:", exif_text)

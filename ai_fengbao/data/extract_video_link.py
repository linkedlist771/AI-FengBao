import re

raw_html_txt_path = "raw_html.txt"
# www.bilibili.com/video/BV11L4y1t7SR/
pattern = r"www.bilibili.com/video/BV[0-9a-zA-Z]{10}/"
matches = re.findall(pattern, open(raw_html_txt_path, encoding="utf-8").read())
matches = list(set(matches))
with open("video_link.txt", "w", encoding="utf-8") as f:
    for match in matches:
        match = match.replace("www.", "https://www.")
        f.write(match + "\n")
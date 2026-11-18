# This File Converts Videos into mp3 formats(Means in Audio Format)

import os
import subprocess

all_files = os.listdir("D:\\All Coding files\\RAG-Video-Model\\Videos for Model")
for i in all_files:
    word_before_extens = i.split("[")[0]
    new_title = word_before_extens.split(" ｜ ")[0]
    Tutorial_number = word_before_extens.split("#")[1]
    # print(f" {Tutorial_number} {new_title}")

    subprocess.run([
    "ffmpeg",
    "-i", f"D:\\All Coding files\\RAG-Video-Model\\Videos for Model\\{i}",
    f"D:\\All Coding files\\RAG-Video-Model\\Audios_mp3\\{Tutorial_number}_{new_title}.mp3"
])
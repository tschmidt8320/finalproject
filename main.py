import tkinter as tk
import random
from pytube import YouTube
vStreams = YouTube('https://www.youtube.com/watch?v=eYZMxMQE2Uw').streams.filter(adaptive=True).filter(type="video")
aStreams = YouTube('https://www.youtube.com/watch?v=eYZMxMQE2Uw').streams.filter(adaptive=True).filter(type="audio")
subtypeChoice = input("mp4 or webm ????\n")[:1].lower()
if subtypeChoice == "m":
    vStreams = vStreams.filter(subtype="mp4")
    subtypeChoice = "mp4"
elif subtypeChoice == "w":
    vStreams = vStreams.filter(subtype="webm")
    subtypeChoice = "webm"

vStreams = list(vStreams)

for x in vStreams:
    if x.video_codec[:4] == "av01":
        vStreams.remove(x)
        
print("resolution/fps?")

for x in vStreams:
    print(str(vStreams.index(x) + 1) + ". " + x.resolution + str(x.fps))
    
vStream = vStreams[int(input()) - 1]

aStreams = aStreams.filter(subtype=subtypeChoice)

print("audio bitrate?")
for x in aStreams:
    print(str(aStreams.index(x) + 1) + ". " + str(x.abr))
    
aStream = aStreams[int(input()) - 1]
    
# vStreams[0].download(output_path="C:/Users/tschmidt8320/Desktop/dcode/youtubedownloader/mdownloads")

"""
for x in aStreams:
    print(x.abr)
"""
"""
window = tk.Tk()

window.columnconfigure(0, weight=1, minsize=75)
window.rowconfigure([0, 1], weight=1, minsize=40)

def rollDie():
    lbl_rollValue["text"] = f"{random.randint(1, 6)}"

lbl_rollValue = tk.Label(text="Click Roll to roll the die")
lbl_rollValue.grid(row=0, column=0, sticky="nsew")

btn_roll = tk.Button(text="Roll", command=rollDie)
btn_roll.grid(row=1, column=0, sticky="nsew")

window.mainloop()
"""
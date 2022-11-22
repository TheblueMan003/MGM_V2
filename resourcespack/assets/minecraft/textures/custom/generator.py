from PIL import Image, ImageDraw
import os

for file in os.listdir("."):
    if (file.endswith(".png")):
        img = Image.open(file)
        if img.size == (16,16):
            back = Image.open("../lootbox_ui/slot.png")
            img = img.resize((48,48))
            back.paste(img,(8,8),img)
            back.save(f"../lootbox_ui/{file}")
            print(file)

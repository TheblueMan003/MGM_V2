import os
from PIL import Image, ImageDraw, ImageFont

lock = Image.open(f"lock_icon.png")

f = open("../../../../../../resources/games.csv")
c = 0
for line in f.readlines()[1:]:
    data = line.split(";")

    out = Image.open(f"{data[0]}_normal.png")
    draw = ImageDraw.Draw(out)

    out.save(f"{data[0]}_normal.png")

    gray = out.convert("LA")
    gray = gray.convert("RGBA")
    gray = Image.alpha_composite(gray, lock)
    gray.save(f"{data[0]}_locked.png")

    draw = ImageDraw.Draw(out)
    draw.rectangle((0,0,512,288), outline=(0,255,255,255), width = 10)
    out.save(f"{data[0]}_selected.png")
    c+=1
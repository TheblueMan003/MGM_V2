import os

lst = ""
for file in os.listdir("."):
    if (file.endswith(".png") and file.startswith("particle_")):
        name = file.replace(".png","")
        s = name.replace("particle_","")
        lst += name +","
        print(f"{name};\"Gold Gift\";gold;\"custom/{name}\";\"lootbox_ui/{name}.png\";\"Click to equip\";pass;particle.select_{s};true;-1;10;0")

print(lst)
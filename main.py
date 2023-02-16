import amulet
import readWorld
import render

mode = str(input("Render textures(t) or heightmap?(h)\n"))
xPos = int(input("X position\n"))
yPos = int(input("Y position\n"))
size = int(input("how big should the map be?(in blocks)\n"))
name = str(input("what should the image be called?\n"))

print("Loading level... this may take some time")
world = amulet.load_level("world") #load the level
level = readWorld.getBlocks(xPos, yPos, size, world) #read world

print("Rendering...")
if mode == "t":
    render.renderTextures(level, size, "./textures/vanilla/block/", 16).save(name + ".png")
elif mode == "h":
    render.renderHeightMap(level, size).save(name + ".png")

world.save()
world.close() #save and close the level

#-122 ,69, -836
import amulet
import readWorld
import render

xPos = input("Enter x position\n") #ask user for size/position for the map
yPos = input("Enter y position\n")
size = input("Enter size of the map\n")
name = input("What do you want to name the image?\n")

level = amulet.load_level("world") #load the level
print("Reading world... \nThis may take some time")
world = readWorld.getBlocks(int(xPos), int(yPos), int(size), level)

print("Rendering...") #render the level
render.renderHeightMap(world, int(size), str(name))

level.save()
level.close() #save and close the level

#xPos, yPos = -122 - 100, -836 - 100
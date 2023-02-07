from PIL import Image, ImageDraw

def renderHeightMap(world, size, name):
    img = Image.new("RGB", (size, size), "white") #setup the image 
    draw = ImageDraw.Draw(img)
    y = 0
    for j in range(size):
        for i in range(size):
            draw.point((i, j), (world[y], world[y], world[y])) #draw a pixel in a grid for each height given for the heightmap
            y += 1

    img.save(str(name)+".png") #save the image
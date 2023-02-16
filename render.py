from PIL import Image, ImageDraw, ImageOps
import os

def renderHeightMap(level, size):
    img = Image.new("RGB", (size, size), "white") #setup the image 
    draw = ImageDraw.Draw(img)
    k = 0
    for j in range(size):
        for i in range(size):
            draw.point((i, j), (level[1][k], level[1][k], level[1][k])) #draw a pixel in a grid for each height given for the heightmap
            k += 1

    return(img)

def renderBlock(img, block, blockName, i, j, res, height):
    height = int(height / 3)
    if os.path.exists(block + "_top.png"): #if a block exists and uses multiple textures it will use blockname_top.png, otherwise just use the block
        texture = Image.open(block + "_top.png").convert("RGB")
    else:
        texture = Image.open(block + ".png").convert("RGB")
    
    if blockName == "grass_block": #if block is grass, change the colour from the gray resource pack to a proper colour
        r, g, b = texture.split()
        r = r.point(lambda i: i-66+height) #changing the rgb values
        g = g.point(lambda i: i-37+height)
        b = b.point(lambda i: i-105+height)
        texture = Image.merge("RGB", (r, g, b))
    
    if blockName == "oak_leaves": #if block is grass, change the colour from the gray resource pack to a proper colour
        r, g, b = texture.split()
        r = r.point(lambda i: i-66+height) #changing the rgb values
        g = g.point(lambda i: i-37+height)
        b = b.point(lambda i: i-105+height)
        texture = Image.merge("RGB", (r, g, b))

    if blockName == "water_flow": #if block is grass, change the colour from the gray resource pack to a proper colour
        r, g, b = texture.split()
        r = r.point(lambda i: i-76+height) #changing the rgb values
        g = g.point(lambda i: i-56+height)
        b = b.point(lambda i: i-8+height)
        texture = Image.merge("RGB", (r, g, b))

    img.paste(texture, (i*res, j*res))

def renderTextures(level, size, texturesDir, res):
    img = Image.new("RGB", (size*res, size*res), "white") #setup the image 
    k = 0

    for j in range(size): #draw a texture for every block given in level
        for i in range(size):
            block = texturesDir + level[0][k].split(":")[0].split("[")[0]
            blockName = level[0][k].split(":")[0].split("[")[0]
            renderBlock(img, block, blockName, i, j, res, level[1][k])
            k += 1
            
    return(img)

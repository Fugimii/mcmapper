from PIL import Image, ImageDraw, ImageOps
import os

blockColours = {
    "grass_block": (145, 189, 89),
    "oak_leaves": (145, 189, 89),
    "jungle_leaves": (145, 189, 89),
    "acacia_leaves": (145, 189, 89),
    "dark_oak_leaves": (145, 189, 89),
    "water_flow": (68, 175, 245),
    "birch_leaves": (128, 167, 85),
    "spruce_leaves": (97, 153, 97)
}

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

    if blockName in blockColours:
        r, g, b = texture.split()
        r = r.point(lambda i: i - 147 + blockColours.get(blockName)[0]) #changing the rgb values
        g = g.point(lambda i: i - 147 + blockColours.get(blockName)[1])
        b = b.point(lambda i: i - 147 + blockColours.get(blockName)[2])
        texture = Image.merge("RGB", (r, g, b))

    img.paste(texture, (i*res, j*res))

def renderTextures(level, size, texturesDir, res):
    img = Image.new("RGB", (size*res, size*res), "white") #setup the image 
    k = 0

    print(level)

    for j in range(size): #draw a texture for every block given in level
        for i in range(size):
            block = texturesDir + level[0][k].split(":")[0].split("[")[0]
            blockName = level[0][k].split(":")[0].split("[")[0]
            renderBlock(img, block, blockName, i, j, res, level[1][k])
            k += 1
            
    return(img)

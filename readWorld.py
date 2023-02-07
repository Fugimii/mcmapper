import amulet
from amulet.utils.world_utils import block_coords_to_chunk_coords

def getBlockAt(xPos, yPos, zPos, level):
    chunkX, chunkZ = block_coords_to_chunk_coords(xPos, zPos) #find the chunk coordinates of the blocks
    chunk = level.get_chunk(chunkX, chunkZ, "minecraft:overworld")
    offset_x, offset_z = xPos - 16 * chunkX, zPos - 16 * chunkZ #find the offset inside the chunk
    block_id = chunk.blocks[offset_x, yPos, offset_z] #get the block id
    universal_block = chunk.block_palette[block_id] #turn the id into a name
    return(universal_block)

def getHighestBlock(xPos, zPos, level):
    for i in range(384):
        yTestPos = 384 - i + 61
        block = getBlockAt(xPos, yTestPos, zPos, level)
        if not str(block) == "universal_minecraft:air" and not ("universal_minecraft:plant") in str(block):
            break
    return(block, yTestPos)

def getBlocks(xPos, yPos, plus, level):
    world = []
    for j in range(plus):
        for i in range(plus):
            block = getHighestBlock(xPos + i, yPos + j, level)
            world.append(block[1])
    return(world)
#-122, 69, -836

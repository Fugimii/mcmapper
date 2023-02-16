import amulet
from amulet.utils.world_utils import block_coords_to_chunk_coords

blockedBlocks = ["air", "grass", "tall_grass", "kelp", "daisy", "allium", "poppy", "blue_orchid", "azure_bluet", "tulip",
                 "oxeye_daisy", "cornflower", "lily_of_the_valley", "wither_rose", "dandelion", "sugar_cane"]

def getBlockAt(xPos, yPos, zPos, level):
    chunkX, chunkZ = block_coords_to_chunk_coords(xPos, zPos) #find the chunk coordinates of the blocks
    chunk = level.get_chunk(chunkX, chunkZ, "minecraft:overworld")
    offset_x, offset_z = xPos - 16 * chunkX, zPos - 16 * chunkZ #find the offset inside the chunk
    block_id = chunk.blocks[offset_x, yPos, offset_z] #get the block id
    universal_block = chunk.block_palette[block_id] #turn the id into a name
    java_block, java_block_entity, java_extra = level.translation_manager.get_version("java", (1, 19, 3)).block.from_universal(universal_block)
    
    return(str(java_block))

def getHighestBlock(xPos, zPos, level):
    for i in range(384):
        yTestPos = 384 - i + 61
        block = getBlockAt(xPos, yTestPos, zPos, level).split(":")[1].split("[")[0].replace("wood", "log").replace("water", "water_flow")
        if not block in blockedBlocks:
            break

    return([block, yTestPos])

def getBlocks(xPos, zPos, plus, level):
    world = []
    heightmap = []
    for j in range(plus):
        for i in range(plus):
            block = getHighestBlock(xPos + i, zPos + j, level)
            world.append(block[0])
            heightmap.append(block[1])

    return([world, heightmap])
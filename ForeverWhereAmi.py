import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getTilePos()
    mc.postToChat(pos.x)
    mc.postToChat(pos.y)
    mc.postToChat(pos.z)
    mc.postToChat("==============")

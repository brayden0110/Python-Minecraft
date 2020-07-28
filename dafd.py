from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.setBlocks(x-25,y-1,z-2000005,x+2500000000000,y-1,z+20000000000,57)

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:41:52 2020

@author: appedu
"""

print("Minecraft")
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

print()
print(mc.player.getTilePos())
mc.player.setTilePos(-245,64,243)
time.sleep(5)
x = 254
y = 69
z = 220
mc.player.setTilePos(x,y,z)
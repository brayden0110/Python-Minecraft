# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:15:45 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(100):
    x,y,z(x-i,y-1,z-i,x+i,y+i,z+i,46)
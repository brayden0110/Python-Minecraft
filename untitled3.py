# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:46:14 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getTilea Pos()
    mc.setBlock(x,y,z,8)
    time.sleep(0.5)
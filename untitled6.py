# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:04:00 2020

@author: appedu
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x+3,y,z,7)
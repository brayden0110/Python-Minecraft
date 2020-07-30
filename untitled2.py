# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:54:39 2020

@author: appedu
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
while True:
    mc.executeCommand("time add 50")
    time.sleep (0.05)
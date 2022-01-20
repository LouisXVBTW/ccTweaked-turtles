from operator import le
import binvox_rw
import sys
import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from numpy import load
np.set_printoptions(threshold=sys.maxsize)

with open("D:\\Windows\\Documents\Computing\\repos\\ccTweaked-turtles\\models\\tinySkull.binvox", "rb") as f:
    skull = binvox_rw.read_as_3d_array(f)

print(type(skull.data))
data = skull.data
print (data.shape)

#print(data[:, 1])
this = data[:]
count = 0
for level in range(0,9):
    print('LEVEL ', level)
    #print (this[level])
    for row in range(0,9):
        print('ROW ', row)
        #print (this[level][row])
        for block in range(0,9):
            if data[level][row][block] == True:
                print(data[level][row][block])
                count += 1
print(count)
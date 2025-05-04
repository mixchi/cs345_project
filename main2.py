import sys
import numpy as np

import h5utils

if (len(sys.argv) != 2):
    print("Usage: "+str(sys.argv[0])+" <input npy matrix> ")
    sys.exit(1)

gridloader = h5utils.load3D()
biggrid = gridloader.loadGrid(sys.argv[1])

print(biggrid.shape)
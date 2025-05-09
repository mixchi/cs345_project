import sys
import os
import numpy as np

import h5utils

if (len(sys.argv) != 3):
    print("Usage: "+str(sys.argv[0])+" <inputDir> <outputDir>")
    sys.exit(1)

gridloader = h5utils.dataInitializer()

# OPTIONAL: the processGrids function returns the location of which it saves the 
# npy data file for all grids.  Assign this to a variable if desired for the next step
npydata = gridloader.processGrids(sys.argv[1], sys.argv[2])

# create the 3D grid from the npy data file (specified in the previous line)
biggrid = gridloader.loadGrid(npydata)

print(biggrid.shape)
import sys
import os
from pathlib import Path
import numpy as np

# stupid workaround to import the h5utils package from a parent directory
sys.path.append(str(Path(__file__).parent.absolute().parent.absolute()))

import h5utils

class checklevels():

    def getIndexOfMolecule(self, molecule):
        index = np.where(self.labels == molecule)[0]
        return index

    def findValidMoleculeLevel(self, molecule):
        moleculeIndex = self.getIndexOfMolecule(molecule)
        levels = self.grid.shape[2] # get number of height levels
        
        for height in range(levels):
            target = self.grid[moleculeIndex, :, height]
            percentnan = np.sum(~np.isnan(target)) / target.size
            print("Height level "+str(height)+": "+str(percentnan)+"%")
        # X, y = self.genXy(molecule, height)

    def __init__(self, inputnpy):

        gridloader = h5utils.dataInitializer()

        # load the big 3D grid with labels
        self.grid, self.labels = gridloader.loadGrid(inputnpy)

        print("Grid shape: "+str(self.grid.shape))
        print("Number of labels: "+str(self.labels.size))
        print(self.labels)


if (len(sys.argv) != 2):
    print("Usage: "+str(sys.argv[0])+" <inputnpy>")
    sys.exit(1)

check = checklevels(sys.argv[1])
target = input("Input molecule from above list: ")
check.findValidMoleculeLevel(target)
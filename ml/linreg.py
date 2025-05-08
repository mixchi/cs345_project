import sys
import os
from pathlib import Path
import numpy as np

# stupid workaround to import the h5utils package from a parent directory
sys.path.append(str(Path(__file__).parent.absolute().parent.absolute()))

import h5utils

class linreg():

    def parseMolecule(self, molecule):
        return molecule

    def __init__(self, inputnpy):

        gridloader = h5utils.dataInitializer()

        # load the big 3D grid with labels
        self.h5array, self.labels = gridloader.loadGrid(inputnpy)

        ### Parameters ###

        print("Grid shape: "+str(self.h5array.shape))
        print("Number of labels: "+str(self.labels.size))
        print(self.labels)


if (len(sys.argv) != 2):
    print("Usage: "+str(sys.argv[0])+" <inputnpy>")
    sys.exit(1)

linreg = linreg(sys.argv[1])
linreg.parseMolecule("HCN")
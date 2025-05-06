import sys
import os
from pathlib import Path
import numpy as np

# stupid workaround to import the h5utils package from a parent directory
sys.path.append(str(Path(__file__).parent.absolute().parent.absolute()))

import h5utils

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Usage: "+str(sys.argv[0])+" <inputDir> <outputDir>")
        sys.exit(1)

    gridloader = h5utils.dataInitializer()

    npydata = gridloader.processGrids(sys.argv[1], sys.argv[2])

    # load an np array of h5file objects
    h5array = gridloader.loadh5(npydata)

    print("Number of h5files: "+str(h5array.size))
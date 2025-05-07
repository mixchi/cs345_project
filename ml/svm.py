import sys
import os
from pathlib import Path
import numpy as np

# stupid workaround to import the h5utils package from a parent directory
sys.path.append(str(Path(__file__).parent.absolute().parent.absolute()))

import h5utils

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: "+str(sys.argv[0])+" <inputnpy>")
        sys.exit(1)

    gridloader = h5utils.dataInitializer()

    # load the big 3D grid with labels
    h5array, labels = gridloader.loadGrid(sys.argv[1])

    print("Grid shape: "+str(h5array.shape))
    print("Number of labels: "+str(labels.size))
    print(labels)
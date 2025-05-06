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

    # load an np array of h5file objects
    h5array = gridloader.loadh5(sys.argv[1])

    print("Number of h5files: "+str(h5array.size))
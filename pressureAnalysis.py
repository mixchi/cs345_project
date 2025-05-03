import sys
import numpy as np

import h5utils

def __init__():
    if (len(sys.argv) != 2):
        print("Usage: "+str(sys.argv[0])+" <input directory>")
        sys.exit(1)

    inputDir = sys.argv[1]

    fileioprocessor = h5utils.fileio()

    # get all files to be processed in iterable array
    files = fileioprocessor.search(inputDir)

    # creating a array which will store pressures from each file
    pressures = []
    loc = 0

    # process each file
    for file in files:
        h5obj = h5utils.h5file(file)
        filteredTable = h5utils.process(h5obj)

        pressure = h5obj.getPressure()
        grid = h5obj.getGrid()

        pressureMask = h5utils.pressureMask()

        rpressure, rgrid = pressureMask.reduceGrid(pressure, grid)

        print("\nold\n", grid.shape, "\nprocessed\n", rgrid.shape)

if __name__ == "__main__": __init__()

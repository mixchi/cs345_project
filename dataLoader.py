import sys
import os
import numpy as np

import h5utils

def __init__():
    if (len(sys.argv) != 3):
        print("Usage: "+str(sys.argv[0])+" <input directory> <output directory>")
        sys.exit(1)

    inputDir = sys.argv[1]
    outputDir = sys.argv[2]

    fileioprocessor = h5utils.fileio()

    # get all files to be processed in iterable array
    files = fileioprocessor.search(inputDir)

    # creating a array which will store h5 object from each file
    h5files = np.empty(len(files), dtype=object)
    loc = 0

    # process each file
    for file in files:
        h5obj = h5utils.h5file(file)
        filteredTable = h5utils.process(h5obj)

        pressure = h5obj.getPressure()
        grid = h5obj.getGrid()

        pressureMask = h5utils.pressureMask()

        rpressure, rgrid = pressureMask.reduceGrid(pressure, grid)
        h5obj.setProcessed(rpressure, rgrid)
        print("Processing "+str(file)+"\t"+str(rgrid.shape))

        h5files[loc] = h5obj
        loc+=1

    np.save(os.path.join(outputDir, "h5files.npy"), h5files)

if __name__ == "__main__": __init__()

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

    # creating a array which will later store pressures from each file
    pressures = []
    loc = 0

    # process each file
    for file in files:
        h5obj = h5utils.h5file(file)
        filteredTable = h5utils.process(h5obj)

        pressures.append(h5obj.getPressure())

        print(h5obj.getPressure())
        print(h5obj.getFilename(), h5obj.getGridShape(), h5obj.getMolecule())

    # pressures = np.stack(pressures)
    # print(pressures.shape)

if __name__ == "__main__": __init__()

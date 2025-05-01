import sys
import numpy as np

import h5utils

def __init__():
    if (len(sys.argv) != 2):
        print("Usage: "+str(sys.argv[0])+" <input directory>")
        sys.exit(1)

    inputDir = sys.argv[1]

    fileioprocessor = h5utils.fileio()

    files = fileioprocessor.search(inputDir)
    pressures = np.zeros(len(files))
    loc = 0
    for file in files:
        h5obj = h5utils.h5file(file)
        filteredTable = h5utils.process(h5obj)

        pressures = np.append(pressures, h5obj.getPressure())

        print(h5obj.getFilename(), h5obj.getGridShape(), h5obj.getMolecule())

if __name__ == "__main__": __init__()

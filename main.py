import os
import sys
from pathlib import Path
import numpy as np

from h5utils.io.fileio import *
from h5utils.h5.h5file import h5file
from h5utils.gridutils.process import *

def main():
    if (len(sys.argv) != 3):
        print("Usage: "+str(sys.argv[0])+" <input directory> <output directory>")
        sys.exit(1)

    inputDir = sys.argv[1]
    outputDir = sys.argv[2]

    fileioprocessor = fileio()

    files = fileioprocessor.search(inputDir)
    for file in files:
        h5obj = h5file(file)
        filteredTable = process(h5obj)

        print(h5obj.getFilename(), h5obj.getGridShape(), h5obj.getMolecule())


    # outputFile = os.path.join(outputDir, os.path.basename(inputFile))+".csv"
    # # print(inputFile, outputFile)

    # h5obj = h5file.load(inputFile)

    # writeCSV(outputFile, h5obj.bigtable)

if __name__ == "__main__": main()
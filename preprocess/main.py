import os
import sys
from pathlib import Path
import numpy as np

import loadfile
import filter
import h5file
import fileWriter

def main():
    if (len(sys.argv) != 3):
        print("Usage: "+str(sys.argv[0])+" <input file> <output directory>")
        sys.exit(1)

    inputFile = sys.argv[1]
    outputDir = sys.argv[2]

    outputFile = os.path.join(outputDir, os.path.basename(inputFile))+".csv"
    # print(inputFile, outputFile)

    h5obj = h5file.load(inputFile)

    fileWriter.writeCSV(outputFile, h5obj.bigtable)

if __name__ == "__main__": main() 
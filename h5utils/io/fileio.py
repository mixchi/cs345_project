import sys
import os
from pathlib import Path

from h5utils.h5.h5file import h5file

class fileio():
    def search(self, inputDir):
        print("Searching for HDF5 files using extension .he5")
        fileList = list(Path(inputDir).rglob("*.[hH][eE]5"))
        return fileList

    def writeCSV(self, outputFile, table):
        np.savetxt(outputFile, table, delimiter=",")
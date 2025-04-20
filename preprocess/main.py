import os
import sys
from pathlib import Path
import h5py
import numpy as np

import loadfile
import filter

# Assign filter
def assignFilter(molecule):
    match molecule:
        case 'BrO':
            return filter.BrOFilter()

        case 'CH3Cl':
            return filter.CH3ClFilter()

        case 'CH3CN':
            return filter.CH3CNFilter()

        case 'ClO':
            return filter.ClOFilter()

        case 'CO':
            return filter.COFilter()

        case 'GPH':
            return filter.GPHFilter()

        case 'H2O':
            return filter.H2OFilter()

        case 'HCl':
            return filter.HClFilter()

        case 'HCN':
            return filter.HCNFilter()

        case 'HNO3':
            return filter.HNO3Filter()

        case 'HO2':
            return filter.HO2Filter()

        case 'HOCl':
            return filter.HOClFilter()

        case 'IWC':
            return filter.IWCFilter()

        case 'N2O':
            return filter.N2OFilter()

        case 'O3':
            return filter.O3Filter()

        case 'OH':
            return filter.OHFilter()

        case 'RHI':
            return filter.RHIFilter()

        case 'SO2':
            return filter.SO2Filter()

        case 'Temperature':
            return filter.TFilter()

        case _:
            raise ValueError('Unknown molecule filter type specified')

def process(h5file):
    dataset = loadfile.LoadFile(h5file)
    pfilter = assignFilter(dataset.product)

    filtered = pfilter.filterGrid(dataset)

    bigtable = np.concatenate((filtered, dataset.lat[:,None]), axis=1)
    bigtable = np.concatenate((bigtable, dataset.lon[:,None]), axis=1)
    bigtable = np.concatenate((bigtable, dataset.time[:,None]), axis=1)

    return bigtable

def saveFile(table, filename):
    np.savetxt(filename, table, delimiter=",")

def main():
    if (len(sys.argv) != 3):
        print("Usage: "+str(sys.argv[0])+" <input file> <output directory>")
        sys.exit(1)

    inputFile = sys.argv[1]
    outputDir = sys.argv[2]

    outputFile = os.path.join(outputDir, os.path.basename(inputFile))+".csv"
    # print(inputFile, outputFile)

    h5file = h5py.File(inputFile, 'r')

    grid = process(h5file)

    saveFile(grid, outputFile)

if __name__ == "__main__": main() 
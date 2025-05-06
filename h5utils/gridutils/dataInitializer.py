import sys
import os
from pathlib import Path
import numpy as np
from collections import defaultdict

import h5utils

class dataInitializer():

    def processGrids(self, inputDir, outputDir):

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
            h5obj.setGrid(filteredTable)

            pressure = h5obj.getPressure()
            grid = h5obj.getGrid()

            pressureMask = h5utils.pressureMask()

            rpressure, rgrid = pressureMask.reduceGrid(pressure, grid)
            h5obj.setProcessed(rpressure, rgrid)
            print("Processing "+str(file)+"\t"+str(rgrid.shape))

            h5files[loc] = h5obj
            loc+=1

            # np.savetxt("./output3/"+str(h5obj.getMolecule()+".csv"), h5obj.getGrid(), delimiter=",")

        save = os.path.join(outputDir, "h5files.npy")
        print("Saving results to disk to "+str(save))
        np.save(save, h5files)
        print("Done")
        return save

    def loadGrid(self, inputFile):
        inputnpy = inputFile

        X = np.load(inputnpy, allow_pickle=True)

        # sort h5file objects by time (first value in time array per file)
        Xsorted = np.array(sorted(X, key=lambda h5file: h5file.getTime()[0]))

        # store each file by molecule type in dictionary
        Xgrouped = defaultdict(list)
        for h5 in Xsorted:
            key = h5.getMolecule()
            Xgrouped[key].append(h5)

        # stack grids vertically per molecule type
        Xtype_grids = {
            type_key: np.vstack([h5.getProcessedGrid() for h5 in h5file])
            for type_key, h5file in Xgrouped.items()
        }

        # combine all molecule types from dictionary into a 3D grid
        big3D = np.stack([grid for grid in Xtype_grids.values()], axis=0)

        return big3D

    # load the npy data file as np array of h5file objects.
    def loadh5(self, inputnpy):
        h5array = np.load(inputnpy, allow_pickle=True)

        return h5array

    # TODO TBD
    def splitnpy(self, inputnpy):
        h5array = np.load(inputnpy, allow_pickle=True)

        for h5obj in np.nditer(h5array, op_dtypes=['object']):
            print(h5obj.getMolecule())
        
        # return h5array
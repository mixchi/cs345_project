import sys
from pathlib import Path
import numpy as np
from collections import defaultdict

import h5utils

class load3D():

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
import sys
import os
from pathlib import Path
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# stupid workaround to import the h5utils package from a parent directory
sys.path.append(str(Path(__file__).parent.absolute().parent.absolute()))

import h5utils

class linreg():

    def getIndexOfMolecule(self, molecule):
        index = np.where(self.labels == molecule)[0]
        return index

    def genXy(self, molecule, height):
        moleculeIndex = self.getIndexOfMolecule(molecule)

        y = np.rot90(self.grid[moleculeIndex, :, height], 1)
        
        X = np.rot90(self.grid[:, :, height], 1)
        X = np.delete(X, moleculeIndex, 1)

        return X, y

    def linreg(self, molecule, height):
        X, y = self.genXy(molecule, height)
        print(X.shape, y.shape)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5)

        lr = LinearRegression()
        lr.fit(X_train, y_train)

        mae_test = mean_absolute_error(y_test, y_pred)
        print(f"MAE test: {mae_test}")

    def __init__(self, inputnpy):

        gridloader = h5utils.dataInitializer()

        # load the big 3D grid with labels
        self.grid, self.labels = gridloader.loadGrid(inputnpy)

        print("Grid shape: "+str(self.grid.shape))
        print("Number of labels: "+str(self.labels.size))
        print(self.labels)


if (len(sys.argv) != 2):
    print("Usage: "+str(sys.argv[0])+" <inputnpy>")
    sys.exit(1)

linreg = linreg(sys.argv[1])

# usage: <molecule> <height level>
linreg.linreg("N2O", 0)
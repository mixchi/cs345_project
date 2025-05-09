import sys
import os
from pathlib import Path
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.preprocessing import StandardScaler #(For standardizing data before training)
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV

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

        print(y[:20])
        print(X[:5, :])

        mask = ~np.isnan(y).flatten()
        X = X[mask]
        y = y[mask]

        non_nan_cols = ~np.isnan(X).all(axis=0)
        X = X[:, non_nan_cols]

        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5)

        linreg = make_pipeline(SimpleImputer(strategy='mean'), LinearRegression())

        linreg.fit(X_train, y_train)

        y_pred = linreg.predict(X_test)

        mae = mean_absolute_error(y_test, y_pred)  # Mean Absolute Error
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)  # Root Mean Squared Error
        r2 = r2_score(y_test, y_pred)  # R-squared

        print(f"MAE: {mae:.15f}, RMSE: {rmse:.15f}, R²: {r2:.4f}")


        '''
        alphas = np.logspace(-4, 2, 20)
        param_grid = {'ridge__alpha': alphas}

        grid = GridSearchCV(linreg, param_grid, cv=5, scoring='r2')

        grid.fit(X_train, y_train)

        best_model = grid.best_estimator_
        y_pred = best_model.predict(X_test)

        print(best_model)

        mean_test_scores = grid.cv_results_['mean_test_score']
        plt.figure(figsize=(8, 5))
        plt.semilogx(alphas, mean_test_scores, marker='o', markersize=3)
        plt.xlabel('Alpha')
        plt.ylabel('Accuracy')
        plt.title('Alpha vs R2 Score')
        plt.grid(True)
        plt.show()

        for alpha, score in zip(alphas, mean_test_scores):
            print(f"Alpha: {alpha:.5f} \t R² Score: {score:.5f}")
'''  
        
        #lr = LinearRegression()
        #lr.fit(X_train, y_train)

        #mae_test = mean_absolute_error(y_test, y_pred)
        #print(f"MAE test: {mae_test}")s

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
linreg.linreg("BrO", 12)
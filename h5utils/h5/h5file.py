import numpy as np
import h5py

from h5utils.filter.filter import *

class h5file():
    def __init__(self, inputFile):
        self.filename = inputFile

        h5file = h5py.File(inputFile, 'r')
        molecule = np.array(h5file['HDFEOS']['SWATHS'])[0]

        self.product = molecule
        self.filter = assignFilter(self)

        self.convergence = np.array(h5file['HDFEOS']['SWATHS'][molecule]['Data Fields']['Convergence'])
        self.status = np.array(h5file['HDFEOS']['SWATHS'][molecule]['Data Fields']['Status'])
        self.quality = np.array(h5file['HDFEOS']['SWATHS'][molecule]['Data Fields']['Quality'])
        self.l2gpPrecision = np.array(h5file['HDFEOS']['SWATHS'][molecule]['Data Fields']['L2gpPrecision'])

        self.grid = np.array(h5file['HDFEOS']['SWATHS'][molecule]['Data Fields'][molecule])

        self.pressure = np.array(h5file['HDFEOS']['SWATHS'][molecule]['Geolocation Fields']['Pressure'])
        self.lat = np.array(h5file['HDFEOS']['SWATHS'][molecule]['Geolocation Fields']['Latitude'])
        self.lon = np.array(h5file['HDFEOS']['SWATHS'][molecule]['Geolocation Fields']['Longitude'])
        self.time = np.array(h5file['HDFEOS']['SWATHS'][molecule]['Geolocation Fields']['Time'])

        self.grid_apriori = np.array(h5file['HDFEOS']['SWATHS'][molecule+"-APriori"]["Data Fields"][molecule+"-APriori"])
        
    def getGridShape(self):
        return self.grid.shape

    def getGrid(self):
        return self.grid

    def getFilename(self):
        return self.filename

    def getMolecule(self):
        return self.product

    def getFilter(self):
        return self.filter

    def getLats(self):
        return self.lat

    def getLons(self):
        return self.lon

    def getTime(self):
        return self.time

    def getPressure(self):
        return self.pressure
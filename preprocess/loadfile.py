import numpy as np
import h5py

import filter

class LoadFile:
        
    def __init__(self, h5file, molecule):
        self.type = molecule

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

        
        
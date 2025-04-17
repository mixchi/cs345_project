import numpy as np
        
class BrOFilter():
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 2.3
        self.maxPressure = 10
        self.minQuality = 1.3
        self.maxConvergence = 1.05

    def filterPressure(self, pressure):
        mask = np.where(pressure >= self.minPressure, 1, 0) & np.where(pressure <= self.maxPressure, 1, 0)
        return mask

    def filterL2GPPrecision(self, l2gp):
        mask = np.where(l2gp > self.minL2GPPrecision, 1, 0)
        return mask

    def filterAPriori(self, apriori):
        mask = np.where(apriori >= self.minAPriori, 1, 0)
        return mask

    def filterQuality(self, quality):
        mask = np.where(quality > self.minQuality, 1, 0)
        return mask

    def filterConvergence(self, convergence):
        mask = np.where(convergence < self.maxConvergence, 1, 0)
        return mask

    def filterGrid(self, h5file):
        linearMask, layersMask = h5file.grid.shape
    
        grid = h5file.grid

        grid = grid * self.filterPressure(h5file.pressure)
        grid = grid * self.filterL2GPPrecision(h5file.l2gpPrecision)
        grid = grid * self.filterAPriori(h5file.grid_apriori)
        grid = grid * self.filterQuality(h5file.quality)[:, None]
        grid = grid * self.filterConvergence(h5file.convergence)[:, None]

        return grid

class CH3ClFilter():
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 4.6
        self.maxPressure = 147
        self.minQuality = 1.3
        self.maxConvergence = 1.05

    def filterPressure(self, pressure):
        mask = np.where(pressure >= self.minPressure, 1, 0) & np.where(pressure <= self.maxPressure, 1, 0)
        return mask

    def filterL2GPPrecision(self, l2gp):
        mask = np.where(l2gp > self.minL2GPPrecision, 1, 0)
        return mask

    def filterAPriori(self, apriori):
        mask = np.where(apriori >= self.minAPriori, 1, 0)
        return mask

    def filterQuality(self, quality):
        mask = np.where(quality > self.minQuality, 1, 0)
        return mask

    def filterConvergence(self, convergence):
        mask = np.where(convergence < self.maxConvergence, 1, 0)
        return mask

    def filterGrid(self, h5file):
        linearMask, layersMask = h5file.grid.shape
    
        grid = h5file.grid

        grid = grid * self.filterPressure(h5file.pressure)
        grid = grid * self.filterL2GPPrecision(h5file.l2gpPrecision)
        grid = grid * self.filterAPriori(h5file.grid_apriori)
        grid = grid * self.filterQuality(h5file.quality)[:, None]
        grid = grid * self.filterConvergence(h5file.convergence)[:, None]

        return grid



    



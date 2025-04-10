import numpy as np

class Filter:
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.mask = None

    def filterPressure(self, pressure, min, max):
        mask = np.where(pressure >= min, 1, 0) & np.where(pressure <= max, 1, 0)
        return mask

    def filterL2GPPrecision(self, l2gp):
        mask = np.where(l2gp > self.minL2GPPrecision, 1, 0)
        return mask

class BrOFilter(Filter):
    def __init__(self):
        super().__init__()

        self.minPressure = 2.3
        self.maxPressure = 10
        self.minQuality = 1.3
        self.maxConvergence = 1.05

    def filterPressure(self, pressure):
        return super().filterPressure(pressure, self.minPressure, self.maxPressure)

    



import numpy as np

def assignFilter(h5file):
    match h5file.product:
        case 'BrO':
            return BrOFilter()

        case 'CH3Cl':
            return CH3ClFilter()

        case 'CH3CN':
            return CH3CNFilter()

        case 'ClO':
            return ClOFilter()

        case 'CO':
            return COFilter()

        case 'GPH':
            return GPHFilter()

        case 'H2O':
            return H2OFilter()

        case 'HCl':
            return HClFilter()

        case 'HCN':
            return HCNFilter()

        case 'HNO3':
            return HNO3Filter()

        case 'HO2':
            return HO2Filter()

        case 'HOCl':
            return HOClFilter()

        case 'IWC':
            return IWCFilter()

        case 'N2O':
            return N2OFilter()

        case 'O3':
            return O3Filter()

        case 'OH':
            return OHFilter()

        case 'RHI':
            return RHIFilter()

        case 'SO2':
            return SO2Filter()

        case 'Temperature':
            return TFilter()

        case _:
            raise ValueError('Unknown molecule filter type specified')

class Filter():
    def filterPressure(self, pressure):
        mask = np.where(pressure >= self.minPressure, 1, np.nan) 
        mask = mask * np.where(pressure <= self.maxPressure, 1, np.nan)
        return mask

    def filterL2GPPrecision(self, l2gp):
        mask = np.where(l2gp > self.minL2GPPrecision, 1, np.nan)
        return mask

    def filterStatus(self, status):
        mask = np.where(status % 2 == 0, 1, np.nan)
        return mask

    def filterAPriori(self, apriori):
        mask = np.where(apriori >= self.minAPriori, 1, np.nan)
        return mask

    def filterQuality(self, quality):
        mask = np.where(quality > self.minQuality, 1, np.nan)
        return mask

    def filterConvergence(self, convergence):
        mask = np.where(convergence < self.maxConvergence, 1, np.nan)
        return mask

    def filterGrid(self, h5file):
        linearMask, layersMask = h5file.getGridShape()
    
        grid = h5file.getGrid()

        grid = grid * self.filterPressure(h5file.pressure)
        grid = grid * self.filterL2GPPrecision(h5file.l2gpPrecision)
        grid = grid * self.filterAPriori(h5file.grid_apriori)
        grid = grid * self.filterQuality(h5file.quality)[:, None]
        grid = grid * self.filterConvergence(h5file.convergence)[:, None]

        return grid

class BrOFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 2.3
        self.maxPressure = 10
        self.minQuality = 1.3
        self.maxConvergence = 1.05

class CH3ClFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 4.6
        self.maxPressure = 147
        self.minQuality = 1.3
        self.maxConvergence = 1.05

    def filterStatus(self, status):
        mask = np.where(status == 0, 1, np.nan)
        return mask

class CH3CNFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 1.0
        self.maxPressure = 147
        self.minQuality = 1.4
        self.maxConvergence = 1.05

    def filterStatus(self, status):
        mask = np.where(status == 0, 1, np.nan)
        return mask

class ClOFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 1.0
        self.maxPressure = 147
        self.minQuality = 1.3
        self.maxConvergence = 1.05

    def filterStatus(self, status):
        mask = np.where(status == 0, 1, np.nan)
        return mask

class COFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 0.001
        self.maxPressure = 215
        self.minQuality = 1.5
        self.maxConvergence = 1.03

class GPHFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 0.00046
        self.maxPressure = 261
        self.minQuality = 0.2
        self.maxConvergence = 1.03

class H2OFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 0.001
        self.maxPressure = 316
        self.minQuality = 0.7
        self.maxConvergence = 2.0

class HClFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 0.32
        self.maxPressure = 100
        self.minQuality = 1.5
        self.maxConvergence = 1.03

class HCNFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 0.1
        self.maxPressure = 21
        self.minQuality = 0.2
        self.maxConvergence = 2.0

class HNO3Filter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 1.5
        self.maxPressure = 215
        self.minQuality = 0.8
        self.maxConvergence = 1.03

    def filterStatus(self, status):
        mask = np.where(status == 0, 1, np.nan)
        return mask

class HO2Filter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 0.046
        self.maxPressure = 22
        self.minQuality = 0.8
        self.maxConvergence = 1.1

    # HO2 can be used irrespective to quality value
    def filterQuality(self, quality):
        mask = np.ones(quality.shape)
        return mask

class HOClFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 2.2
        self.maxPressure = 10
        self.minQuality = 1.2
        self.maxConvergence = 1.05

class IWCFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 83
        self.maxPressure = 215
        self.minQuality = 0.9
        self.maxConvergence = 1.03

class N2OFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 0.46
        self.maxPressure = 100
        self.minQuality = 0.8
        self.maxConvergence = 2.0

class O3Filter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 0.001
        self.maxPressure = 261
        self.minQuality = 1.0
        self.maxConvergence = 1.03

class OHFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 0.0032
        self.maxPressure = 32
        self.minQuality = 1.0
        self.maxConvergence = 1.1

    # OH can be used irrespective to quality value
    def filterQuality(self, quality):
        mask = np.ones(quality.shape)
        return mask

class RHIFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 0.001
        self.maxPressure = 316
        self.minQuality = 0.7
        self.maxConvergence = 1.03

class SO2Filter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 10.0
        self.maxPressure = 215
        self.minQuality = 0.95
        self.maxConvergence = 1.03

class TFilter(Filter):
    def __init__(self):
        self.minL2GPPrecision = 0
        self.statusModFilter = 1
        self.minAPriori = 0
        self.minPressure = 0.00046
        self.maxPressure = 261
        self.minQuality = 0.2
        self.maxConvergence = 1.03
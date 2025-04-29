import filter
import loadfile
import numpy as np
import h5py

class load():
    # Assign filter
    def assignFilter(self, molecule):
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

    def process(self, grids):
        
        moleculeFilter = self.assignFilter(grids.product)
        filtered = moleculeFilter.filterGrid(grids)

        bigtable = np.concatenate((filtered, grids.lat[:,None]), axis=1)
        bigtable = np.concatenate((bigtable, grids.lon[:,None]), axis=1)
        bigtable = np.concatenate((bigtable, grids.time[:,None]), axis=1)

        return bigtable

    def __init__(self, inputFile):
        h5file = h5py.File(inputFile, 'r')

        self.grids = loadfile.LoadFile(h5file)
        self.bigtable = self.process(self.grids)
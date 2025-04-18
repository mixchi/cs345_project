import h5py
import numpy as np

import loadfile
import filter

# Assign filter
def assignFilter(molecule):
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

def process(h5file):
    dataset = loadfile.LoadFile(h5file)
    pfilter = assignFilter(dataset.product)

    filtered = pfilter.filterGrid(dataset)

    bigtable = np.concatenate((filtered, dataset.lat[:,None]), axis=1)
    bigtable = np.concatenate((bigtable, dataset.lon[:,None]), axis=1)
    bigtable = np.concatenate((bigtable, dataset.time[:,None]), axis=1)

    return bigtable

def main():

    # Testing with BrO
    file = "sample/MLS-Aura_L2GP-CH3Cl_v05-03-c01_2025d001.he5"
    h5file = h5py.File(file, 'r')

    grid = process(h5file)

if __name__ == "__main__": main() 
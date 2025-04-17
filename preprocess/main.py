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

        case _:
            raise ValueError('Unknown molecule filter type specified')

def process(h5file, molecule):
    dataset = loadfile.LoadFile(h5file, molecule)
    pfilter = assignFilter(molecule)

    filtered = pfilter.filterGrid(dataset)

    for t in range(10):
        print(dataset.time[t])

    print(filtered.shape, dataset.time.shape)

    bigtable = np.concatenate((filtered, dataset.lat[:,None]), axis=1)
    bigtable = np.concatenate((bigtable, dataset.lon[:,None]), axis=1)
    bigtable = np.concatenate((bigtable, dataset.time[:,None]), axis=1)

    for row in range(20):
        print(bigtable[row])

    print(bigtable.shape)

def main():

    # Testing with BrO
    file = "sample/MLS-Aura_L2GP-CH3Cl_v05-03-c01_2025d001.he5"
    h5file = h5py.File(file, 'r')

    process(h5file, "CH3Cl")

if __name__ == "__main__": main() 
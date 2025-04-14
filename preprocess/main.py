import h5py
import numpy as np

import loadfile
import filter

# Testing with BrO

file = "sample/MLS-Aura_L2GP-BrO_v05-03-c01_2025d001.he5"
h5file = h5py.File(file, 'r')

molecule = 'BrO'
brO = loadfile.LoadFile(h5file, molecule)

brOfilter = filter.BrOFilter()
filtered = brOfilter.filterGrid(brO)

for row in range(20):
    print(filtered[row])

print(filtered.shape)

# l2gpMask = brOfilter.filterL2GPPrecision(brO.l2gpPrecision)
# print(l2gpMask)
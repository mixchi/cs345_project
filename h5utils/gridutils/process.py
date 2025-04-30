import numpy as np

def process(h5obj):
        
    moleculeFilter = h5obj.getFilter()
    filtered = moleculeFilter.filterGrid(h5obj)

    # bigtable = np.concatenate((filtered, h5obj.getLats()[:,None]), axis=1)
    # bigtable = np.concatenate((bigtable, h5obj.getLons()[:,None]), axis=1)
    # bigtable = np.concatenate((bigtable, h5obj.getTime()[:,None]), axis=1)

    return filtered
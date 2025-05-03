import numpy as np

class pressureMask():

    def deleteNanIndexes(self, arr, mask):
        obj = np.where(np.isnan(mask))
        r = np.delete(arr, obj, axis=1)
        return r
    
    def reduceGrid(self, pressure, grid):
        length = pressure.size
        if length == 55:
            head = 36 # resolution until index 36 is double that of std grid
            mask = np.ones(head)
            mask[1::2] = np.nan
            mask = np.concatenate((mask, np.ones(length-head)))

            nan_indexes = np.where(np.isnan(mask))

            pressure = pressure * mask
            grid = grid * mask

            # remove nan values, any column with nan is removed from grid
            pressure = pressure[~np.isnan(pressure)]
            grid = self.deleteNanIndexes(grid, mask)

            return pressure, grid

        else:
            return pressure, grid

            

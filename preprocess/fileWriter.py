import numpy as np

class writeCSV():
    def __init__(self, outputFile, table):
        np.savetxt(outputFile, table, delimiter=",")
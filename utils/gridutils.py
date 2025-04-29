import glob
import sys
import numpy as np

def checkGridSize(file):
    data = np.genfromtxt(file, delimiter=',')
    print(file+"\t"+str(data.shape))

def main():
    for file in glob.glob(sys.argv[1]+"/*"):
        checkGridSize(file)

if __name__ == "__main__": main() 
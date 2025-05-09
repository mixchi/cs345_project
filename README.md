# The CS345 Term Project

### Converting a series of input he5 (HDF) files to a single npy matrix file:

`python datagen.py <input> <output>`

* Input: directory that will be recursively searched for input files
* Output: where a single .npy file will be saved (default filename h5files.npy)

### Using pregenerated h5 npy matrix:
`python ml/linreg.py <input npy>`

* Input: the file path of where the npy file was saved during the previous step
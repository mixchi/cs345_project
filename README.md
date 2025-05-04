# cs345_project
The CS345 Term Project

## Preprocessing example:
See the example.py file in the root.  It does two things:
* find all files in the specified input directory
* output filtered files to the output directory
* save a npy data file of the preprocessing to the output directory for future use (so that preprocessing/filtering doesn't have to be run every time)
* loads the npy data file back in as a 3D grid

Usage: `python example.py inputdir outputdir`
Where inputdir contains all of the h5 files.
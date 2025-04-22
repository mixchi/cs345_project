# Preprocessing

The programs in this directory process HDF5 files by filtering them according to Aura MLS Data Quality Documentation and saves the result to a CSV file.  It is recommended this be run using conda, see the requirements.txt file for required libraries.

**Usage:** `python preprocess/main.py <inputfile> <outputdir>`

For multiple files, combine the python program with the Linux find command: 
`find inputdir/ -name "*.he5" -exec python preprocess/main.py {} outputdir/ \;`

This program only runs on a single thread.  For multi-threading, combine the find command with xargs: `find inputdir/ -name "*.he5" | xargs -n1 -P8 -I{} python preprocess/main.py {} outputdir/`

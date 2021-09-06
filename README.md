# threeXYZgraphing
3d xyz graphing using threejs

# Graphing usage
The main .html file needs an http server to load. For further reference visit https://threejs.org (search for 'How-to-run-things-locally')

# Python
Python version in use = 3.9.0

To list current requirement:
> pip freeze requirement.txt

To install packages in requirement.txt:
> pip install -r requirement.txt

## Algorithms
* nearest_node.py
Reads the .csv input contained in both input/ and perm_output/ folders, then it writes an ordered (shortest distance from nodes starting from the origin) xyz points list in the xyz_output/ folder

* write_permutation.py
Reads the .csv file in the input/ folder and writes a list of permutations in the perm_output/ folder
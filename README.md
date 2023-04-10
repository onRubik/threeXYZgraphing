# threeXYZgraphing
3d xyz graphing using threejs

# Graphing usage
To fix issues when loading threejs modules directly from index.html [Rollup](https://www.npmjs.com/package/rollup) was used.

After cloning the project open its folder with a terminal and install the npm dependencies:
> npm install

In the terminal run the npm rollup script to build the bundle:
> npm run build

To start the http server run the npm script (it will be available locally http://localhost:3000). To open the local URL preferably use Google Chrome:
> npm start

To change the source for the coordinates to load change the path contained in loaderPoints.load() and loaderLine.load() and choose another file contained in the xyz_ouput/ folder.


## View an example
To view "nearest node helix 202" visit:
https://youtu.be/6B0NAUKHD7k


# Python
Python version in use = 3.9.16

To list current requirement:
> pip freeze requirement.txt

To install packages in requirement.txt:
> pip install -r requirement.txt

## Algorithms
* nearest_node.py
Reads the .csv input contained in both input/ and perm_output/ folders, then it writes an ordered (shortest distance from nodes starting from the origin) xyz points list in the xyz_output/ folder

* write_permutation.py
Reads the .csv file in the input/ folder and writes a list of permutations in the perm_output/ folder
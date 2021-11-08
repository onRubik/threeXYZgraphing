from math import *
from read_points import *
from distance_xyz import *
from decimal import Decimal
import csv
import os


def write_permutation():
    
    try:
        list_xyz = read_points()
        script_dir = os.path.dirname(__file__)
        out_csv_path = os.path.join(script_dir, '../perm_output/perm_polygons.csv')

        f = open(out_csv_path, 'w', newline='')
        writer = csv.writer(f)

        # write header for csv ouput
        header_row = ['id1', 'id2', 'distance']
        writer.writerow(header_row)

        for record1 in list_xyz:
            for record2 in list_xyz:
                if(record1 != record2):

                    x0 = Decimal(record1[2])
                    y0 = Decimal(record1[3])
                    z0 = Decimal(record1[4])
                    x1 = Decimal(record2[2])
                    y1 = Decimal(record2[3])
                    z1 = Decimal(record2[4])

                    dist_result = distance_xyz(x0, y0, z0, x1, y1, z1)
                    perm_row = [record1[0], record2[0], dist_result]

                    writer.writerow(perm_row)

        f.close()

    except Exception as e:
        print(e)
    

if __name__ == '__main__':
    write_permutation()
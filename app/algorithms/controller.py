from data_integrity import dataIntegrity
from pathlib import Path
import math
import os
import pandas as pd
import csv
from decimal import Decimal
from numpy import array
from itertools import combinations
import networkx as nx


class controller:
    def __init__(self, chain_name: str):
        self.chain_name = chain_name


    def distanceXyz(self, x0, y0, z0, x1, y1, z1):
        deltaX = x1 - x0
        deltaY = y1 - y0
        deltaZ = z1 - z0
        
        distance = math.sqrt(deltaX * deltaX + deltaY * deltaY + deltaZ * deltaZ)
        
        return distance
    

    def nearestNode(self):
        origin = 1
        file_name = 'perm_polygons.csv'
        xyz_file_name = 'xyz_polygons.txt'
        node_history = []
        node_history.append(origin)

        script_dir = os.path.dirname(__file__)
        full_path = os.path.join(script_dir, '../input/polygons.csv')
        perm_path = os.path.join(script_dir, '../perm_output/' + file_name)
        xyz_path = os.path.join(script_dir, '../xyz_output/' + xyz_file_name)
        out_pd_read = pd.read_csv(perm_path)

        new_headers = ['id', 'type', 'x', 'y', 'z']
        out_points_source = pd.read_csv(full_path,skiprows=-1, names=new_headers)
        i = len(out_points_source)

        origin_filter = out_points_source['id'] == origin
        first_line_tro_write = out_points_source.where(origin_filter)
        i_origin = first_line_tro_write.index[0]
        
        f = open(xyz_path, 'w', newline='')

        f.write(
            str(first_line_tro_write.iloc[i_origin]['x']) + 
            "\t" + 
            str(first_line_tro_write.iloc[i_origin]['y']) + 
            "\t" + 
            str(first_line_tro_write.iloc[i_origin]['z']) + 
            "\n"
        )

        for lines in range(i):
            
            next_node = self.readPermCsv(origin, out_pd_read, node_history)
            filter1 = out_points_source['id'] == next_node
            origin = next_node
            node_history.append(next_node)
            line_to_write = out_points_source.where(filter1)
            next_filter = line_to_write.notnull()
            i_next_write = next_filter[next_filter['id'] == True].index.tolist()[0]
            
            f.write(
                str(line_to_write.iloc[i_next_write]['x']) + 
                "\t" + 
                str(line_to_write.iloc[i_next_write]['y']) + 
                "\t" + 
                str(line_to_write.iloc[i_next_write]['z']) + 
                "\n"
            )


    def readPermCsv(self, origin, out_pd_read, node_history):
        filter1 = out_pd_read['id1'] == origin
        new_set = out_pd_read.where(filter1)
        new_source = new_set[~new_set['id2'].isin(node_history)]
        nearest_node = new_source['distance'].min()
        nearest_node_filter = new_source['distance'] == nearest_node
        filter2_arg = out_pd_read.where(nearest_node_filter)
        filter_not_null = filter2_arg.notnull()
        i_next_node = filter_not_null[filter_not_null['id1'] == True].index.tolist()[0]
        result_min = out_pd_read.iat[i_next_node, 1]
        
        return result_min
    

    def readPoints(self):
        script_dir = os.path.dirname(__file__)

        full_path = os.path.join(script_dir, '../input/polygons.csv')

        with open(os.path.join(full_path), mode = 'r')as file:
            
            rows_read_csv = []

            csv_file = csv.reader(file)
            for lines in csv_file:
                rows_read_csv.append(lines)

        return rows_read_csv
    

    def writePermutation(self):
        list_xyz = self.readPoints()
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

                    dist_result = self.distanceXyz(x0, y0, z0, x1, y1, z1)
                    perm_row = [record1[0], record2[0], dist_result]

                    writer.writerow(perm_row)

        f.close()

    
    def mst(self):
        xyz_output, os_type = dataIntegrity.imgFolder(self)
        xyz_output = Path(xyz_output)
        xyz_output = xyz_output.parent

        if os_type == 'Windows':
            xyz_output_fix = str(xyz_output) + '\\xyz_output\\' + self.chain_name
        if os_type == 'Linux':
            xyz_output_fix = str(xyz_output) + '/xyz_output/' + self.chain_name
        pass


    def getDistance(self):
        xyz_input, os_type = dataIntegrity.imgFolder(self)
        xyz_input = Path(xyz_input)
        xyz_input = xyz_input.parent

        if os_type == 'Windows':
            xyz_input_fix = str(xyz_input) + '\\input\\' + self.chain_name + '.csv'
        if os_type == 'Linux':
            xyz_input_fix = str(xyz_input) + '/input/' + self.chain_name + '.csv'
        
        points = dict()
        distances = dict()
        df_csv = pd.read_csv(xyz_input_fix)
        for x in df_csv:
            print(x)
        # for i in range(len(arr)):
        #     points[i] = {'x':arr[i][0], 'y':arr[i][1]}

        # comb = combinations(points.keys(),2)
        # for x in comb:
        #     x_1 = points[x[0]]['x']
        #     x_2 = points[x[1]]['x']
        #     y_1 = points[x[0]]['y']
        #     y_2 = points[x[1]]['y']
        #     distances[x] = math.sqrt((x_2-x_1)**2 + (y_2-y_1)**2)

        # return points, distances

        pass
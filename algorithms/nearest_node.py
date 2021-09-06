from read_perm_csv import *
import pandas as pd
import os


def write_xyz():
    try:
        origin = 1
        file_name = 'perm3.csv'
        xyz_file_name = 'xyz1.txt'
        node_history = []
        node_history.append(origin)

        script_dir = os.path.dirname(__file__)
        full_path = os.path.join(script_dir, '../input/shortPoints.csv')
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
            
            next_node = read_perm_csv(origin, out_pd_read, node_history)
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
            
    except Exception as e:
        print(e)


if __name__ == '__main__':
    write_xyz()
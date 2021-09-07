import csv
import os


def read_points():
    script_dir = os.path.dirname(__file__)

    full_path = os.path.join(script_dir, '../input/helix_202.csv')

    with open(os.path.join(full_path), mode = 'r')as file:
        
        rows_read_csv = []

        csv_file = csv.reader(file)
        for lines in csv_file:
            rows_read_csv.append(lines)

    return rows_read_csv


if __name__ == '__main__':
    read_points()
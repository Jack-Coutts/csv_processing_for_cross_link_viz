import csv
import argparse


def initiate_parser():

    parser = argparse.ArgumentParser(description='''Create csv containing cross-link info for Pymol. 
                                                    IMPORTANT: Sequence positions must be in columns 2 and 5! 
                                                    EXAMPLE:  python(3) cross_link_csv.py 
                                                    --input_file /Users/couttsj/Desktop/sarah/X-links.csv 
                                                    --output_file /Users/couttsj/Desktop/sarah/output_file.csv''')

    parser.add_argument('--input_file', type=str, required=True, help='''Add file path for input csv 
                                                                            e.g. desktop/test_folder/test_file.txt''')
    parser.add_argument('--output_file', type=str, required=True, help='''Add file path for output csv 
                                                                            e.g. desktop/test_folder/test_file.txt''')

    args = parser.parse_args()

    file_path_in = args.input_file
    out_file_path = args.output_file

    return file_path_in, out_file_path


def read_input_csv_file(file_path):  # Read input csv file

    with open(file_path) as f:
        reader = csv.reader(f, delimiter=',')  # Read in file
        next(reader, None)  # Skip headers
        data = [row for row in reader]  # Nested list where each sublist is a row

    return data


def new_list(nested_list):  # Retain relevant columns, convert to int, subtract 24, add |A|

    output_list = []  # Initiate new list
    for row in nested_list:  # Iterate over each row
        output_list.append([f'{int(row[1])-24}|A|{int(row[4])-24}|A|'])  # Create each of the output rows
    return output_list


def create_output_csv(output_list, output_file_path):

    with open(output_file_path, "wt") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(output_list)


def run_script():
    file_path_in, out_file_path = initiate_parser()
    read_in = read_input_csv_file(file_path_in)
    out_list = new_list(read_in)
    create_output_csv(out_list, out_file_path)


# Run the Script
try:
    run_script()
    print('Script Success!')
except:
    print('Script Failure! Check help documentation: python(3) cross_link_csv.py -h.')



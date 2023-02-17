# Usage Instructions

Download the python script called cross_link_csv.py from this repository.

When using the Command Prompt (Windows) or Terminal (Mac) type the dir (Windows) or ls (Mac) 
command to check what files are in the current folder/directory. The cd command followed by a directory/folder name 
can be used to navigate into another folder E.g. cd Desktop

Assuming you want your input CSV file is called: my_csv_file
Assuming you want your output CSV to be called:: my_output_file

1. Place your input CSV file into a folder with the python script called cross_link_csv.py.
2. Open Terminal/Command Prompt and navigate to the folder containing the python script and input CSV file.
3. Run the python script using the one of the following commands (depending on your system): 
   - python3 cross_link_csv.py --input_file my_csv_file.csv --output_file my_output_file.csv
   - python cross_link_csv.py --input_file my_csv_file.csv --output_file my_output_file.csv
4. If the script runs successfully you should see the message 'Script Success!'. If not you will see 'Script Failure!'.
5. To get help with running the python script type the command: python3 cross_link_csv.py -h or python cross_link_csv.py -h
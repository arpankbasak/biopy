import subprocess

dir_list = subprocess.check_output( ['ls', '-l'] )

import csv
lines = list(csv.reader( dir_list.split("\n"), delimiter = " " ))
file_lines = [x for x in lines if len(x) == 9]
python_files = [x for x in file_lines if x[8][-3:] == '.py']
python_file_names = map(lambda x: x[8].upper(), python_files)
print "\n".join(python_file_names)


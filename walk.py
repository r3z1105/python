#!/usr/bin/python
import os
import fnmatch
my_list = []
dirs = '/home/r3z1105/pystuff'
pattern = '*.py'
output = '/home/r3z1105/output.txt'
for paths, subdirs, files in os.walk(dirs):
    for filename in fnmatch.filter(files, pattern):
        my_list.append(os.path.join(paths, filename))
        print(my_list)
        with open(output, 'w') as f_obj:
            for i in my_list:
                f_obj.write(str([i]))

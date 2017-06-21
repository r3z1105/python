#!/usr/bin/python3
import os
import fnmatch
import stat
my_list = []
dirs = '/home/'
output = '/home/r3z1105/output.txt'
for paths, subdirs, files in os.walk(dirs):
    for x in files:
        my_list.append(os.path.join(paths, x))
        with open(output, 'w') as f_obj:
            for i in my_list:
                f_obj.write(str([i]))
    for files in my_list:
        print(files)
        print(stat.filemode(os.stat(files).st_mode))

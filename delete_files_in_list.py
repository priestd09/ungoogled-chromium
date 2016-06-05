#!/usr/bin/env python

# Delete files in list generated by generate_cleaning_list.sh
# This script is designed to run cross-platform
# Usage: delete_files_in_list.py file_list

import sys
import os
import os.path

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print "Usage: {} file_list".format(sys.argv[0])
        exit(1)
    file_list_path = sys.argv[1]

    with open(file_list_path) as file_list:
        for line in file_list:
            line = line.replace("\n", "")
            if len(line) > 0:
                line = os.path.normpath(line)
                if os.path.isfile(line):
                    os.remove(line)
                else:
                    print "Not a file: {}".format(line)
    print "Done evaluating {}".format(file_list_path)
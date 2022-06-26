import os, glob
from typing import Dict, List
import copy
import shutil

def converter(files: List, all_switch: Dict, only_switch: Dict, windows=True, debug = True):
    if windows:
        separator = '\\'
    else:
        separator = r"/"

    temp_files = []

    for file in files:
        temp_file = copy.copy(file)
        address = file.split(separator)

        """ name's separator should be selected here! """
        name_separator = "_"
        if int(address[-1].split(name_separator)[-2]) == 26:
            temp_file = os.path.join(all_switch[address[0]], only_switch[address[1]], address[2], address[3])
        else:
            temp_file = os.path.join(all_switch[address[0]], address[1], address[2], address[3])

        temp_files.append(temp_file)

        if debug != True:
            os.makedirs(os.path.dirname(temp_file), exist_ok = True)
            shutil.copyfile(file, temp_file)
        else:
            print(temp_files)

if __name__ == "__main__":
    files = glob.glob(os.path.join('before', '**', '*.png'), recursive=True)
    all_swtich = {"before":"after"}
    only_switch = {"train":"test"}
    converter(files, all_swtich, only_switch)
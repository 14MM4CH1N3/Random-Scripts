import os
import re

workingdr = ""
pattern = ""
replacement = ""

os.chdir(workingdr)
for dir_name in os.listdir('.'):
    if dir_name.find(pattern) != -1:
        print(dir_name)
        new_dir = "./" + dir_name.replace(pattern, replacement)
        old_dir = "./" + dir_name
        os.rename(old_dir, new_dir)
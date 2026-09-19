import os
from pathlib import Path

def batch_rename_extensions(directory_path, old, new):
    for filename in os.listdir(directory_path):
        if old in filename:
            new_filename = filename.replace(old, new)
            
            old_file_path = os.path.join(directory_path, filename)
            new_file_path = os.path.join(directory_path, new_filename)
            
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: '{filename}' to '{new_filename}'")
        ##
    ##
##

batch_rename_extensions("./", "success", "player")

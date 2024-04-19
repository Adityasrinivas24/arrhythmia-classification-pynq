#Script to rename images in both folders

import os

data_folder = './ecgdataset'
arr_folder = os.path.join(data_folder, 'arr')
nsr_folder = os.path.join(data_folder, 'nsr')

# Rename files in 'arr' folder
for i, filename in enumerate(sorted(os.listdir(arr_folder)), start=1):
    old_path = os.path.join(arr_folder, filename)
    new_filename = f'arr_{i}.png'
    new_path = os.path.join(arr_folder, new_filename)
    os.rename(old_path, new_path)

# Rename files in 'nsr' folder
for i, filename in enumerate(sorted(os.listdir(nsr_folder)), start=1):
    old_path = os.path.join(nsr_folder, filename)
    new_filename = f'nsr_{i}.png'
    new_path = os.path.join(nsr_folder, new_filename)
    os.rename(old_path, new_path)

print("Files renamed successfully.")

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:36:54 2022

@author: talha

directories, files & paths management utilities. 'dfpu'
"""
import re, os, glob, shutil
import numpy as np
from tqdm import tqdm, trange
from utils.directorytree import DirectoryTree

numbers = re.compile(r'(\d+)')


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def get_all_files(main_dir, sort=True):
    '''
    Parameters
    ----------
    main_dir : absolute/relative path to root directory containing all files.
    sort : wether to sort the output lost in Alphabetical order.
    
    Returns
    -------
    file_list : list containing full paths of all files.
    
    '''

    file_list = []
    for root, dirs, files in os.walk(main_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    if sort:
        file_list = sorted(file_list, key=numericalSort)

    return file_list


def get_all_dirs(main_dir, sort=True):
    '''
    Parameters
    ----------
    main_dir : absolute/relative path to root directory containing all files.
    sort : wether to sort the output lost in Alphabetical order. 
    
    Returns
    -------
    dir_list : list containing full paths of all sub directories in root.
    
    '''

    dir_list = []
    for root, dirs, files in os.walk(main_dir):
        for dr in dirs:
            dir_list.append(os.path.join(root, dr))
    if sort:
        dir_list = sorted(dir_list, key=numericalSort)

    return dir_list


def get_num_of_files(main_dir):
    '''
    Parameters
    ----------
    main_dir : absolute/relative path to root directory containing all files.
    
    Returns
    -------
    A Dictionary containing follwoing keys/info;
    files_in_sub_dirs : an array containing number of file in all sub dirs of root.
    sub_dirs : name of all the sub-dirs/classes inside the root.
    total_files : total number of files in all the sub-dir/classes.
    
    '''   
    file_count = []
    for root, dirs, files in os.walk(main_dir):
        file_count.append((os.path.basename(os.path.normpath(root)), len(files)))
    
    if len(file_count) > 1: # if the main_dir have sub_dirs
        file_count = file_count[1:]
        
        name_classes = np.asarray(file_count)[:,0].astype(str)
        num_per_class = np.asarray(file_count)[:,1].astype(int)
        
        total_files = sum(num_per_class)
        
        dir_prop = {'sub_dirs':name_classes, 'files_in_sub_dirs':num_per_class,
                    'total_files':total_files}
    else: # if the main_dir don't have sub_dirs
        total_files = file_count[0][1]
        
        dir_prop = {'sub_dirs':None, 'files_in_sub_dirs':None,
                    'total_files':total_files}
    
    return dir_prop


def get_basename(full_path, include_extension=True):
    '''
    Parameters
    ----------
    full_path : absolute/relative path of file or dir.
    include_extension : if the input full_path leads to file the by default the
                        the file's extension in included in output string.
                        
    Returns
    -------
    name : name of the file with/without extension or the base dir
    
    '''
    
    name = os.path.basename(os.path.normpath(full_path))
    if include_extension== False:
        name = name.split('.')[0]
    return name


def get_random_files(main_dir, count=1):
    '''
    Parameters
    ----------
    main_dir :  absolute/relative path to root directory containing all files.
    count : TYPE, optional
        the number of files to get from the root dir. The default is 1.
        
    Returns
    -------
    file_path : absolute path to the file/files.
    
    '''
    
    file_list = get_all_files(main_dir, sort=True)
    file_path = np.random.choice(file_list, size=count, replace=False)
    
    return file_path

def rename_wrt_dirname(main_dir):
    '''
    Change the names of all files inside the main_dir wrt their sub_dir names.
    e.g:
    main_dir
    │
    ├── dir1\
    │   ├── ADE_train_00000983.jpg
    │   ├── ADE_train_00000984.jpg
    │   ├── ADE_train_00000994.png
    │
    ├── dir2\
        ├── ADE_train_00000983.jpg
        └── redme.txt
    
    will change to ->
    main_dir
    │
    ├── dir1\
    │   ├── dir1_001.jpg
    │   ├── dir1_002.jpg
    │   ├── dir1_003.png
    │
    ├── dir2\
        ├── dir2_004.jpg
        └── dir2_005.txt
    
    Parameters
    ----------
    main_dir :  main directory containing all sub dirs.
    -------
    None.

    '''
    main_dir = main_dir +'/'
    x = get_all_files(main_dir)

    for i in trange(len(x), desc="Changing names of files"):
        path = os.path.dirname(x[i])
        ext_name = os.path.basename(x[i]).split('.')[-1]
        new_name = os.path.dirname(x[i]).split('/')[-1] + f'_{i:03d}.' + ext_name
        os.rename(x[i],
                  os.path.join(os.path.dirname(x[i]), new_name))
    return None

def file_name_replacer(data_dir, new_name, name2replace):
    '''
    Changes the names of all files inside a dir by replacing the specific strings
    in old file name with new ones, specified via 2 input lists.
    e.g.
    if:
    new_name = [train, iris]
    name2replace = [new_2, new_3] then, this
    
    ..\test_dir\
    │
    ├── dir1\
    │   ├── ADE_train_00000983.jpg
    │   ├── ADE_train_00000984.jpg
    │   ├── ADE_train_00000994.png
    ├── dir2\
    │   ├── sub_dir1\
    │   │   └── sub_sub_dir1\
    │   │       ├── housing.csv
    │   │       ├── iris.csv
    │   │       ├── mnist_test_300.csv
    │   │       └── mnist_train_3000.csv
    
    will change to ->
    
    \test_dir\
    │
    ├── dir1\
    │   ├── ADE_new_2_00000983.jpg
    │   ├── ADE_new_2_00000984.jpg
    │   ├── ADE_new_2_00000994.png
    ├── dir2\
    ├── sub_dir1\
    │   └── sub_sub_dir1\
    │       ├── housing.csv
    │       ├── mnist_new_2_3000.csv
    │       ├── mnist_test_300.csv
    │       └── new_3.csv
    
    Note : both lists should have same length
    Parameters
    ----------
    data_dir : main dir containig all the sub dir.
    new_name : list containing the new names which will replace the old ones.
    name2replace : list containing the strings which will be replaced wiht new ones.

    Returns
    -------
    None.

    '''
    full_paths = get_all_files(data_dir + '/')
    
    k_name = name2replace
    e_name = new_name
    
    new_full_paths = []
    
    for i in full_paths:
        name = os.path.basename(i)
        for j in range(len(k_name)):        
            temp = name.replace(k_name[j], e_name[j])
            name = temp
        #new_names.append(name)
        
        new_full_paths.append(os.path.join(os.path.dirname(i), name)) 
    [os.rename(full_paths[c], new_full_paths[c]) for c in range(len(full_paths))]
    
    return None


def del_all_files(main_dir, confirmation=True):
    '''
    Parameters
    ----------
    main_dir : absolute/relative path to root directory containing all files.
    confirmation : TYPE, optional
        confirm before deleting the files. The default is True.
        
    Returns
    -------
    None.
    
    '''
    
    file_list = get_all_files(main_dir, sort=True)
    if confirmation:
        ans = input(f'do you wnat to continue deleting {len(file_list)} files? [yes[y]/no[n]] \n')
    else:
        ans = 'y'
    if ans == 'y':
        for i in file_list:
            os.remove(i)
        n = len(file_list)
        print(f'{n} files deleted.')
    else:
        print('Operation stopped.')
    return


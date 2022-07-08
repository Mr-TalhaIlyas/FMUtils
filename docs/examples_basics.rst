================
Examples: 
================

A standard use case for DirectoryTree Generator
------------------------------------------------

The following example shows a standard use case. :: python

    from fmutils import directorytree as fdt

    dt = fdt.DirectoryTree(root_dir='..Downloads/test_dir', dir_only=False,
                    write_tree=True)
    dt.generate()

    # or clone the dir tree at another location

    fdt.clone_dir_tree('/Downloads/test_dir/', '/Downloads/test_dir2/')


A Use case for getting the list of dirs
-----------------------------------------

The following example shows a simple example to get the list of all the sub-dirs in the root dir. :: python

    from fmutils import fmutils as fmu

    d_list = fmu.get_all_dirs(main_dir = '../Downloads/test_dir/', sort=True)

    print(d_list)

Plotting Data Dist
-------------------
The following example shows a simple example to get the bar plot of files present inside the root dir. :: python

    from fmutils import plottingutils as fpu

    df = fpu.plot_data_dist('../Downloads/test_dir/', sort=None).
    
Train Validation Test Split
----------------------------
The following example shows a simple example to get the bar plot of files present inside the root dir. :: python

    from fmutils import fmutils as fmu

    fmu.tvt_split(img_dir, dest_dir, lbl_dir=None, test_split=0.2, val_split=0.1, mode='copy')

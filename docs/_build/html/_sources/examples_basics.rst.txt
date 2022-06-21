================
Examples: 
================

A standard use case for DirectoryTree Generator
-------------------

The following example shows a standard use case. ::

    from fmutils.directorytree import DirectoryTree

    dt = DirectoryTree(root_dir='..Downloads/test_dir', dir_only=False,
                    write_tree=True)
    dt.generate()


A Use case for getting the list of dirs
-----------------------------------------

The following example shows a simple example to get the list of all the sub-dirs in the root dir. ::

    from fmutils import fmutils as fmu

    d_list = fmu.get_all_dirs(main_dir = '../Downloads/test_dir/', sort=True)

    print(d_list)

Plotting Data Dist
-------------------
The following example shows a simple example to get the bar plot of files present inside the root dir. ::

    from fmutils import fmutils as fmu

    fmu.plot_data_dist('../Downloads/test_dir/', sort=None).


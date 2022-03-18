# FMUtils
File Management Utilities, for easily accessing and managing large number of files and dirs in ML datasets.


## Usage

```python
from fmutils.directorytree import DirectoryTree

dt = DirectoryTree(root_dir='..Downloads/test_dir', dir_only=False,
                   write_tree=True)
dt.generate()
```
### output
```
directory tree file saved at 
 ../dir_tree.txt
```
inside text file
```
C:\Users\talha\Downloads\test_dir\
│
├── dir1\
│   ├── ADE_train_00000983.jpg
│   ├── ADE_train_00000984.jpg
│   ├── ADE_train_00000994.png
│   ├── ADE_train_00000995.jpg
│   ├── ADE_train_00001021.jpg
│   ├── ADE_train_00001022.jpg
│   ├── ADE_train_00001022.png
│   └── redme.txt
│
├── dir2\
│   ├── sub_dir1\
│   │   └── sub_sub_dir1\
│   │       ├── housing.csv
│   │       ├── iris.csv
│   │       ├── mnist_test_300.csv
│   │       └── mnist_train_3000.csv
│   │
│   │
│   └── sub_dir2\
│
│
├── dir3\
│   ├── index_ade20k.mat
│   ├── _annotations.txt
│   ├── __9t72HlzHdWWgOQSZVv8A.json
│   ├── __IoBfs3I6vB5ND-vqXK1A.json
│   ├── __KhdlKlVCeDQzVU2iyqYA.json
│   ├── __kprvedRGmbZJIfLBNq_w.json
│   ├── __VyXRQL8yDPkUBPTpW19A.xml
│   ├── __xaqDe9h8QfOyxTt0224Q.xml
│   ├── __Y8BcLJ1fhqwMARVgPg7Q.xml
│   ├── __YtZD5n9fhOMe-rzQa5oA.xml
│   └── __ZqCAIYS0qHpupUQoUuEQ.xml
│
└── dir4\
    └── sub_dir1\
        ├── demo.py
        └── Mapillary Vistas Research Edition License.pdf

```

```python
from fmutils import fmutils as fmu

d_list = fmu.get_all_dirs(main_dir = 'C:/Users/talha/Downloads/test_dir', sort=True)

print(d_list)
```

Python program find_rename.py uses glob and os module to look for folders in base directory /shri/distribution/folds and renames the files in the subdirectories.


Current folder/file structure is like this::

root@skamat-Compaq-15-Notebook-PC:~/shri/distribution/folds# tree
.
|-- AAR
|   `-- AAR-rc1.ear
|-- BAR
|   `-- BAR-rc1.ear
|-- CAR
|   `-- CAR-rc1.ear
|-- test_file1
`-- test_file2

 
Expected folder/file structure after we run find_rename.py ::

root@skamat-Compaq-15-Notebook-PC:~/shri/distribution/folds# tree
.
|-- AAR
|   `-- AAR.latest.ear
|-- BAR
|   `-- BAR.latest.ear
|-- CAR
|   `-- CAR.latest.ear
|-- test_file1
`-- test_file2

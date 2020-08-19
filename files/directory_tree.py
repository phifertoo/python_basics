import os

# os.walk() returns the folder, subfolder, and list of filenames
for folderName, subfolders, fileNames in os.walk('../'):
    print('The folder is:' + folderName)
    print('The subfolders in ' + folderName + 'are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are:' + str(fileNames))
import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))

# current directory
current_directory = os.getcwd()
print(current_directory)

# change current directory
os.chdir('C:\\')
current_directory = os.getcwd()
print(current_directory)

# absolute file path
'C:\\Users\\phife\\applications\\automate_the_boring_stuff\\files'

# relative file path is relative to the current directory
'spam.png' 
# translates to
'C:\\Users\\phife\\applications\\automate_the_boring_stuff\\files'

# this folder ./
# parent folder ../
# child folder ./child_folder

# change directory
os.chdir('C:\\Users\\phife\\applications\\automate_the_boring_stuff\\files')

# convert relative file path to an aboslute file path
absolute_path = os.path.abspath('arkansas_directory.pdf')
print(absolute_path)

# directory of a path
directory = os.path.dirname(absolute_path)
print(directory)

# file name (if there is no file, it would return the last folder)
file_name = os.path.basename(absolute_path)
print(file_name)

# list the files and folders in a given folder
contents = os.listdir('../')
print(contents)

# isfile(), isdir(), exists(), getsize()

totalSize = 0
for filename in os.listdir('./'): #for all files/folders in the current folder (./)
    if not os.path.isfile(os.path.join('./', filename)): #if it is not a file, don't add it to total size
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('./', filename))

print(totalSize)

# create new folder using os.makedirs('path + new_folder_name')
new_folder = os.makedirs('./folder1')

# create multiple new folders
new_folder = os.makedirs('./folder1/folder2/folder3')

# to change the directory
# os.chdir('c:\\users\\phife')
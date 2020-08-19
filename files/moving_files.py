import shutil

# path of file to be copied and destination
# shutil.copy('./arkansas_directory.pdf', '../regex/new_name.pdf')

# copy an entire folder and its contents
# shutil.copytree('./, '../regex')

# move a file
# file to be moved, destination
# shutil.move('./arkansas_directory.pdf', '../regex')

# to rename you have to use the .move() to move the file to the current folder with the new name
shutil.move('./arkansas_directory.pdf', './new_name.pdf')

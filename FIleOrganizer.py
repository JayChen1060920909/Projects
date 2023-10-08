import os
import shutil



# This path is adjustable!
path = r"C:\Users\user\Downloads"
files = os.listdir(path)

# Go through every file, we first find the extension(.pdf, .png) first, then we create a folder if these extension folder is not exist
# And we move the file into that folder, to make it much cleaner for all users.
for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
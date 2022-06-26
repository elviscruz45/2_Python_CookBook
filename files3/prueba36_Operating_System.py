# OS Module in python with examples

# The Os module in python provides fuctions for interanting with the operatin system. OS comes under
#Python's standar utility modules. this module provides a protable way of using operatin system-dependent
#functionality. The *os* and *os.path* modules include many functions to interact with the file system.

# HANDLING THE CURRENT WORKING DIRECTORY

#Condifer Current Working Directory (CWD) as a folder, where the Python is operating. Whenever the files are called only
#by their name, Python assumes that it starts int the CWD which means that name-only reference will be successful only if the file
# is in the Python's CWD.
#Note: the folder where the Python script is running is known as the Current directory. this is not the path whre the Python script is located

#To get the location of the current working directory os.getcwd() is used.

#Example:

# Python program to explain os.mkdir() method

# importing os module
import os

# Directory
directory = "GeeksforGeeksaa"

# Parent Directory path
parent_dir = "/Users/elviscruz45/Desktop/2_Python_CookBook"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)

# Directory
directory = "Geeksaa"

# Parent Directory path
parent_dir = "/Users/elviscruz45/Desktop/2_Python_CookBook"

# mode
mode = 0o666

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)


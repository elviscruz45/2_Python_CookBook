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

# Python program to explain os.makedirs() method
	
# importing os module
import os
	
# Leaf directory
directory = "Nikhil"
	
# Parent Directories
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"
	
# Path
path = os.path.join(parent_dir, directory)
	
# Create the directory
# 'Nikhil'
os.makedirs(path)
print("Directory '% s' created" % directory)
	
# Directory 'GeeksForGeeks' and 'Authors' will
# be created too
# if it does not exists
	
# Leaf directory
directory = "c"
	
# Parent Directories
parent_dir = "D:/Pycharm projects/GeeksforGeeks/a/b"
	
# mode
mode = 0o666
	
path = os.path.join(parent_dir, directory)
	
# Create the directory 'c'
	
os.makedirs(path, mode)
print("Directory '% s' created" % directory)
	
	
# 'GeeksForGeeks', 'a', and 'b'
# will also be created if
# it does not exists
	
# If any of the intermediate level
# directory is missing
# os.makedirs() method will
# create them
	
# os.makedirs() method can be
# used to create a directory tree


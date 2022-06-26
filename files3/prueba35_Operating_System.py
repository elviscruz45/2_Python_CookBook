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

# Python program to explain os.getcwd() method
		
# Python program to change the
# current working directory
	
	
import os
	
# Function to Get the current
# working directory
def current_path():
	print("Current working directory before")
	print(os.getcwd())
	print()



# Driver's code
# Printing CWD before
current_path()
	
# Changing the CWD
os.chdir('../')
	
# Printing CWD after
current_path()


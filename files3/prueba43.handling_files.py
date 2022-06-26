# Python program to explain shutil.copy() method

# importing shutil module
import shutil

source = "./hello.txt"
destination ="./main2.txt"

# Copy the content of
# source to destination
dest = shutil.copy(source, destination)

# Print path of newly
# created file
print("Destination path:", dest)

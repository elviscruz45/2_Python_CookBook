import shutil
import os
#shutil.move('./main.txt', './files2')

print(os.listdir())


for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)

import os
filenames = os.listdir('.')
print(filenames)
a=[name for name in filenames if name.endswith(('.c', '.h'))]

any(name.endswith('.py') for name in filenames)


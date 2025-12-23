import subprocess
import os
# open the sample file used
with open('runtimeOptions.properties') as f:
    # read the content of the file opened
    content = f.readlines()
    if content[1] == "debug = 0":
        # Use pythonw to run silently
        subprocess.Popen(['pythonw', 'gui.py'])
    elif content[1] == "debug = 1":
        print("Opened with terminal.")
        os.startfile('gui.py')

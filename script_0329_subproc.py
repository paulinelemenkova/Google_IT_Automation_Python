# ​Python uses I/O streams. ​I/O streams are the basic mechanism for performing input and output operations ​in your programs. You can think of these streams as pathways between your ​programs and their input sources like a keyboard, or output, like the screen.

#import os
#os.chdir("/Users/polinalemenkova/Documents/Python/Scripts_2026")
#os.getcwd()

# Subprocess can run any shell command in Python, providing greater flexibility.
# these commands create a directory.

# Pathlib is most helpful for working extensively with file paths, when you want an object-oriented and intuitive way to handle file system tasks. Pathlib provides an object-oriented approach to handle file system paths. Compared to OS, Pathlib is more intuitive for file and directory operations. Pathlib is more readable for path manipulations.

#Subprocess:

subprocess.run(['mkdir', 'test_dir_subprocess2'])

#OS:

os.mkdir('test_dir_os2')

#Pathlib:

from pathlib import Path
test_dir_pathlib2 = Path('test_dir_pathlib2')

# Subprocess is a powerful module that allows you to do anything you could in Python from within the shell, then get information back into Python. You’ll probably want to stick with OS for basic file and directory operations or Pathlib for working extensively with file paths. But when you interface with external processes, run complex shell commands, or need precise control over input and output, the subprocess module is the way to go.

# ​Python uses I/O streams. ​I/O streams are the basic mechanism for performing input and output operations ​in your programs. You can think of these streams as pathways between your ​programs and their input sources like a keyboard, or output, like the screen.

#import os
#os.chdir("/Users/polinalemenkova/Documents/Python/Scripts_2026")
#os.getcwd()

#cat streams.py
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)

#./streams.py
This will come from STDIN: Python Rocks!
Now we write it to STDOUT: Python Rocks!

cat greeting.txt
Well hello there, STDOUT

cat greeting.txt
Well hello there, STDOUT

ls -z

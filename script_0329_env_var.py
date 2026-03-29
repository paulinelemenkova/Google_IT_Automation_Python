# ​Python uses I/O streams. ​I/O streams are the basic mechanism for performing input and output operations ​in your programs. You can think of these streams as pathways between your ​programs and their input sources like a keyboard, or output, like the screen.

#import os
#os.chdir("/Users/polinalemenkova/Documents/Python/Scripts_2026")
#os.getcwd()

#!/usr/bin/env python3
import os
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

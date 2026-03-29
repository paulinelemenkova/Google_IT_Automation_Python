#import os
#os.chdir("/Users/polinalemenkova/Documents/Python/Scripts_2026")
#os.getcwd()

import subprocess
subprocess.run(["date"])

import subprocess
subprocess.run(["date"])
subprocess.run(["sleep", "2"])

import subprocess
subprocess.run(["date"])
subprocess.run(["sleep", "2"])
result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)

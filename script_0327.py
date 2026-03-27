import os
os.getcwd()
os.chdir("/Users/polinalemenkova/Documents/Python/Scripts_2026")
os.getcwd()
os.listdir("/Users/polinalemenkova/Documents/Python/Scripts_2026/")
os.remove("novel.txt")
os.rename("Script_0325_test.py", "Script_0325_test_1.py")
os.rename("Script_0325_test_1.py", "Script_0325_test.py")
os.path.exists("Script_0325_test.py")
# provide the file size
os.path.getsize("Script_0325_test.py")
# provide a unix timestamp for the file
os.path.getmtime("Script_0325_test.py")
os.mkdir("files_2703")
# returns a list of all the files and sub-directories in ​a given directory
os.listdir("files_2703")
os.listdir("/Users/polinalemenkova/Documents/Python/Scripts_2026/")
#  In Linux and MacOS, the portions of a file are split using a forward ​slash (/). On Windows, they're split using a backslash (\).

# Example: Joining a folder and a filename
path = os.path.join("data", "logs", "daily_report.txt")

print(path)
# On Windows: data\logs\daily_report.txt
# On Unix:    data/logs/daily_report.txt

#--------------------------------------->
# Create a directory and move a file from one directory to another
# using low-level OS functions.

import os

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
 os.mkdir(dest_dir)

# Construct source and destination paths:
src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
dest_file = os.path.join(os.getcwd(), "test1", "README.md")

# Move the file from its original location to the destination:
os.rename(src_file, dest_file)

#---------------------------------------<

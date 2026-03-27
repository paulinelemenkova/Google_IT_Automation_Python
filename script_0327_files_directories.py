# There are 2 ways to manage files and directories in Python:
# to use low-level functions in the OS module that mimics standard Linux commands.
# to use the Pathlib module - an object-oriented interface to working with the file systems.
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

# pathlib 
#--------------------------------------->
from pathlib import Path

# Check to see if the "test1" subdirectory exists. If not, create it:
dest_dir = Path("/Users/polinalemenkova/Documents/Python/Scripts_2026/test2/")
if not dest_dir.exists():
    dest_dir.mkdir()
    
# Construct source and destination paths:
src_file = Path("/Users/polinalemenkova/Documents/Python/Scripts_2026/test1/README.md")
dest_file = dest_dir / "README.md"

# Move the file from its original location to the destination:
src_file.rename(dest_file)
os.listdir("test2")
#---------------------------------------<

#--------------------------------------->
#1. The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file. Fill in the gaps to create a script called "program.py".

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, 'w') as file:
    filesize = file.write(comments)
  return(filesize)

print(create_python_script("program.py"))
#---------------------------------------<

#2. Question 2. The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
os.chdir("/Users/polinalemenkova/Documents/Python/Scripts_2026")
with open (filename, 'w') as file:
    file.write("script_27.py")

  # Return the list of files in the new directory
os.chdir('..')
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))

# 4. --------------------------------------->
# The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open (filename,'w') as file:
    {}
  timestamp = os.path.getmtime(filename)

  # Convert the timestamp into a readable format, then into a string
  timestamp = datetime.datetime.fromtimestamp(timestamp)
 
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{}".format(timestamp.strftime("%Y-%m-%d")))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd

# 3. --------------------------------------->
# 5.
# Question 5  The parent_directory function returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias that means "go up to the parent directory". Fill in the gaps to complete this function.

import os
def parent_directory():
  # Create a relative path to the parent
  # of the current working directory
  relative_parent = os.path.abspath('..')

  # Return the absolute path of the parent directory
  return relative_parent

print(parent_directory())

# There are 2 ways to manage files and directories in Python:
# to use low-level functions in the OS module that mimics standard Linux commands.
# to use the Pathlib module - an object-oriented interface to working with the file systems.
import os
os.getcwd()
os.chdir("/Users/polinalemenkova/Documents/Python/Scripts_2026")

import csv
f = open("csv_file.txt")
# The reader() function of the CSV module will interpret the file as a CSV.
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()

# 2. Generating CSV

import csv

hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
    
with open('hosts.csv') as hosts:
    reader = csv.DictReader(hosts)
    for row in reader:
      print(("{} has {} users").format(row["name"], row["users"]))
      

# 1.Question 1. We're working with a list of flowers and some information about each one. The create_file function writes this information to a CSV file. The contents_of_file function reads this file into records and returns the information in a nicely formatted block. Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a dictionary using DictReader.

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))


# Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process the data without turning it into a dictionary. How do you skip over the header record with the field names?

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    # Read the rows of the file
    rows = csv.reader(file)
    # Process each row
    for row in list(rows)[1:]:
      name, color, types = row
      # Format the return string for data rows only
      return_string += "a {} {} is {}\n".format(color, name, types)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))


with open('employees.csv', "w") as file:
# Pass the file object to the CSV reader
    content = csv.reader(file)

  # Open the file
with open("employees.csv") as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)

with open("employees.csv", mode='r', encoding='utf-8') as csv_file:
    # 2. Pass the file object to DictReader
    reader = csv.DictReader(csv_file)
    
csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')

  employee_list = []
  for data in employee_file:
    employee_list.append(dict(data))
    
return employee_list

employee_list = read_employees('<file_location>')
print(employee_list)


c2_python-operating-system/2_managing-files-with-python/graded-assessment/scripts/generate_report.py

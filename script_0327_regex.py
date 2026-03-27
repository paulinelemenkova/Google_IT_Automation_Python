# There are 2 ways to manage files and directories in Python:
# to use low-level functions in the OS module that mimics standard Linux commands.
# to use the Pathlib module - an object-oriented interface to working with the file systems.
import os
os.getcwd()
os.chdir("/Users/polinalemenkova/Documents/Python/Scripts_2026")
os.getcwd()

%----------------------->
import re
result = re.search(r"aza", "plaza")
print(result)

%----------------------->
import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

%----------------------->

import re

text = "Contact us at support@example.com or sales@company.org"

# Find all email addresses
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

print(emails)
# Output: ['support@example.com', 'sales@company.org']

%----------------------->
import re
print(re.search(r"[Pp]ython", "Python"))

%----------------------->
import re
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

%----------------------->
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

%----------------------->
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

%----------------------->
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
print(re.search(r".com", "welcome"))
print(re.search(r".com", "weeelcome"))

%----------------------->
import re
def check_character_groups(text):
  result = re.search(r"\w+\s+\w+", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

import re
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"A.*a$", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

import re
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

# This line of code matches U.S. phone numbers in the format 111-222-3333.
r”\d{3}-\d{3}-\d{4}”

# This line of code matches any positive or negative number, with or without decimal places.
r”^-?\d*(\.\d+)?$”

# This line of code is often used to extract specific parts of URLs or file paths, such as the directory names or filenames.
r”^/(.+)/([^/]+)/$”

# \s is a shorthand character class that stands for "whitespace."

import re
def contains_acronym(text):
  pattern = "\([A-Z][a-zA-Z0-9]+\)"
  result = re.search(pattern, text)
  return result != None

# The contains_acronym() function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions." Fill in the regular expression in this function:

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

# The check_time() function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case.

import re
def check_time(text):
  pattern = r"^(1[0-2]|[1-9]):[0-5][0-9]\s?(?i)(am|pm)$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False

import re

def check_time(text):
    # Pattern explanation:
    # 1[0-2]|[1-9] -> 10, 11, 12 OR 1-9
    # [0-5][0-9]   -> 00 through 59
    # (?i)         -> Case-insensitive flag
    pattern = r"^(1[0-2]|[1-9]):[0-5][0-9]\s?(?i)(am|pm)$"
    
    return re.search(pattern, text) is not None

# Test Cases
print(check_time("12:45pm"))   # True
print(check_time("9:59 AM"))   # True
print(check_time("01:30pm"))   # False (Leading zero)
print(check_time("13:15am"))   # False (Hour out of range)
print(check_time("5:60am"))    # False (Minutes out of range)

# In regular expressions,\w is a shorthand character class that stands for "word character.

# An intern implemented a zip code checker, but it works only with five-digit zip codes. Your task is to update the checker so that it includes all nine digits of the zip code; the leading five digits and the optional four after the hyphen. The zip code needs to be preceded by at least one space, and cannot be at the start of the text. Update the regular expression.
# This line of code is designed to search for a US Zip Code in either the standard 5-digit format (12345) or the extended 9-digit "Zip+4" format (12345-6789).

# The key to this pattern is the Pipe symbol (|), which acts as an OR operator.
# (Space): It starts with a literal space. This ensures it doesn't match a random string of numbers inside another word (like an ID number ID88342).

import re

def correct_function(text):
  result = re.search(r" \d{5}| \d{5}-\d{4}", text)  # Corrected regex pattern with space
  return result is not None

def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False

# ---------------------------->
# 1. The check_web_address() function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.

import re
def check_web_address(text):
  pattern = r"^[\w\._-]*\.[A-Za-z]*$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

# ---------------------------->
# 2. The check_time() function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?

import re
def check_time(text):
  pattern = r"^(1[0-2]|[1-9]):[0-5][0-9]\s?(?i)(am|pm)$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False

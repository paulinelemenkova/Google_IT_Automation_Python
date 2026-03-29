import os
#os.getcwd()
os.chdir("/Users/polinalemenkova/Documents/Python/Scripts_2026")
os.getcwd()

# While the standard way to run a script is from the Terminal using python3 python.py, you can definitely trigger a script from inside the console using the exec() function or the runpy module.

# Method 1: Using exec() (The Quick Way) The exec() function reads the content of your file and executes it as Python code within your current session.
exec(open("script_0329_reading_data.py").read())

# Method 2: Using runpy (The Cleaner Way). If you want to run the script more formally—as if you had called it from the terminal—the runpy module is a built-in tool designed exactly for this.

import runpy
runpy.run_path("script_0329_reading_data.py")
runpy.run_path("script_0329_time_convert.py")
runpy.run_path("script_0329_standard_streams.py")
runpy.run_path("script_0329_env_var.py")
runpy.run_path("script_0329_inp_fun.py")
runpy.run_path("script_0329_unittest.py")


exec(open("script_0329_unittest.py").read())

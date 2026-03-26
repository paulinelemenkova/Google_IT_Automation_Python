# https://docs.python.org/3/library/venv.html
# To create a virtual environment, open your terminal and navigate to your project's directory. Then, run the following command:

python -m venv myenv

#This command creates a virtual environment named "myenv" in your project directory. To activate the virtual environment, use the appropriate command for your operating system:

. myenv/bin/activate

# Create a virtual environment for each project: Whenever you start a new project, create a new virtual environment. This ensures a clean and isolated workspace. Use requirements files: To document and manage your project's dependencies, create a requirements.txt file. This file lists all the libraries and their versions. You can generate it using

pip freeze > requirements.txt

# and later install them in a new environment using

pip install -r requirements.txt

# Activate and deactivate: Always activate the appropriate virtual environment before working on a project and deactivate it when you're done. This prevents confusion and potential conflicts.

# Virtual environments are your key to maintaining a clean and efficient Python development workflow. By isolating your projects, you can work confidently, test various libraries, and ensure consistency across your codebase

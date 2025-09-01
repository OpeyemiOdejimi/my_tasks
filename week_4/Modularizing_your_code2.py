# Modularizing Your Code 2

# 3. Python Modules
#   * What a module is (a.py file that can be resued)
#   * Importing built_in modules (math, random, datetime)
#   * Writng your own module (creating my_module.py and importing it)
#   * Aliasing modules (import numpy as np)


# What is a Module?
#   * A module in Python is simply a file with .py extension that contains Python code (functiomns, variables, or classes) whoich can be reused in other programs.
#   * Instead opf writing the same code again and agaoin, you can write it once in a module and then import it anywhere.
#   * Lets think of a module as a toolnbox. Each tool (function, variables, or classes) which can be reused in other programs.


# * Importing Built-in Modules

# * Python already comes with many pre-built modules that you canuse directly.
# * Some common examples are:
# * math -for mathematical operations
# * random - for generating random numbers
# * datetime - for working  with datesand time.
# etc.
# To use built in modules, you have to load them into your environment, that is, import them.


# Duiferent Ways to Import Modules

#1. Import the whole module

import math

# Lets put it to use

print(math.sqrt(9))
# - Note that you must specify the module name when calling a function within it.

'''
TypeError
call In[4], line 8
      3 import math
      6 # Lets put it to use
----> 8 print(math.sqrt())
      9 # - Note that you must specify the module name when calling a function within it.

TypeError: math.sqrt() takes exactly one argument (0 given)

'''

# 1. import as an alis

import math as m

# lets put it to use

print(m.sqrt(25))

# - This shirten the module name, this is common with libaries like numpy, pandas, etc

# 3. Import specific functions or variables

from math import sqrt, pi
print(sqrt(36))

# - here you don't need the prefix 'math.' anymore

# 4. Import everything from the module

from math import *

print(sqrt(49))
print(pi)

# - This is usually not recommended because it can cause name conflicts if two modules have functions with same name

# Writing Your Own Module
# - step1: Create a folder. Name it my_module
# - step2: Create a file inside the folder. Name it first.py
# - step3: Create another file inside the same folder. Name it second.py
# - step4: Create another file still inside inside the same folder. Name it main.py

# - here is the fok=lder structure

'''
project_folder/
│
├── my_module/
│   ├── first.py
│   ├── second.py
│   └── main.py

'''
#- Note that anyone with forward slash is a folder while the ones with extensions are the files.

# my_module/first.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
    


# my_module/second.py


def greet(name):
    return f"Hello, {name}! I am creating my own module"

def reverse_string(string):
    return string[::-1]

def count_characters(string):
    return len(string)

def count_words(string):
    return len(string.split())



# my_module/main.py

import first
import second

# lets use the functions in the first.py file

print("=== Math Functions ===")
print("5 + 3 =", first.add(5, 3))
print("10 - 4 =", first.subtract(10, 4))
print("6 * 7 =", first.multiply(6, 7))
print("20 / 5 =", first.divide(20, 5))

# lets use the functions in the second.py file
print("\m=== String Functions ===")
print(second.greet("Ridwan"))
print("Reverse of 'Python' =", second.reverse_string("Python"))
print("Character count in sentence =", second.reverse_string("Python"))
print("Word count in sentence =", second.count_words("Python modules are powerful"))


# 4. Python Packages
#   * What a package is (a folder with init.py)
#   * Installing and using third-party packages (pip install requests, import requests)
#   * Organizing multiple modules into a package


# What is a package?
#   * A package in Python is a way to organize related modules togther into a folder.
#   * Inside this folder, there must be a special file called __init__.py (can be empty). This file tells Python that the folder should be treated as a package.
#   * uhmmm, lets think of a package as a standard mechanic workshop, and each module is a different toolbox inside the workshop. The init.py file is like the label on the workshop telling passerbys that this is a mechanic workshop.

# Do you understand?


# Third-Party Packages
#   * Python comes with some built-in modules, but you can also install extra packagecreated by others.
# These packages are stored in the Python Package Index (PyPi).

# We install them using pip (Python's package manager) or conda a

# How to install Python Packages
# 1. Using pip
#   * This is the most common method.
#   * It installs packages from PyPI. It is the Python's central package repository.

#   * To work with it, you have to use it in ypur terminal.

# pip install requests                  # Install latest version
# pip install requests==2.28            # Install specific version
# pip install --upgrade requests        # Upgrade existing package
# pip unistall requests                 # Remove package


# 2. Using uv
#   * This is the modern, super-fast package and project manager
#   * It is a RUST-based that unifies package installation, virtual environment and Python version management into one fast, modern CLI.
#   * To use uv

# Run this commamnd on yourn terminal depending on your OS
# Recommended method: standalone installer
 # macOS/Linux

# curl -LsSf https://astrial.sh/uv/install.sh | sh

# or

# Windows

# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1  |  iex"

#   * After installation, verify version
# uv --version
#   * Using uv to install packages
#   * But before it works you must have a working virtual environment

# uv add reqquests         # Install package and update project files
# uv pip install flask     # Works like pip but much faster
# uv remove requests       # Uninstall
# uv venv                  # Create a virtual environment automatically
# uv run script.py         # Run scripts in the managed environment



# Other packages managers that you should try exploring

'''
- Other package managers that you should try exploring

| Method                            | Description                     | Best For                                 |
| --------------------------------- | ------------------------------- | ---------------------------------------- |
| `pip install ...`                 | Standard installation from PyPI | Most common and simple use case          |
| `pip install -r requirements.txt` | Batch install from file         | Reproducible projects                    |
| Virtualenv + `pip`                | Isolated environments           | Independent project setups               |
| `conda install ...`               | Data science ecosystem          | Scientific and system-level dependencies |
| Clone + `pip install .`           | Custom or non-PyPI packages     | Local development and experiments        |
| `.whl install`                    | Prebuilt package install        | Faster installations                     |
| `pip install -e .`                | Editable (development) install  | Active package development               |
| `uv ...`                          | All-in-one modern manager       | Speed, simplicity, and full workflow     |
'''

# Creating a virtual Environment

#   * What is a Virtual Environment?

#   * A virtual environment (venv) is an isolated workspaces where you can install and manage Python packages without affecting the global/system Python installation.
#   * Each project can have its own dependencies,, even if they conflict with other projects.
#   * Why should you form the habit of always creating a Venv before starting a project?
#   * It keeps project dependencies separate.
#   * It prevents version conflicts
#   * It makes collaboration easier (everyone uses the same environment).
#   * It is required in many production setups.


# How to create a Virtual Environment
# Create a virtual environment
# python -m venv virtual_environment_name

# This will create a folder inside your working folder with the name "virtual_environment_name"

#   * To use it, you have a activate it.

# 1. Click on the folder
# 2. Look for Script and open it.
# 3. Look for 'activate'
# 4. Right click on it and look for copy relative path
# 5. Click on it.
# 6. Finally to your terminal and select Command prompt then paste the path you copied.

#   * Alternatively, you can use this script.

# virtual_environment_name\Scripts\activate         # For windows
# source virtual_environment_name/bin/activate      # linux or macOS

# Deactivating a virtual Environment

# deactivate

# Saving and Sharing Requirements

# To freeze the installed packages into a file
# pip freeze > requirements.txt

# To install them later
# pip install -r requirements.txt


# Creating Your Package

'''
```
my_project/
│
├── my_package/              # Package folder
│   ├── __init__.py          # Makes this folder a package
│   ├── math_utils.py        # Module 1
│   ├── string_utils.py      # Module 2
│
└── main.py                  # Script that uses the package

```
'''
# goph419lab01
# author: Allison Unruh
#Course:GOPH 419
#Instructor:B. Karchewski 
#Lab purpose: Calculate the range of launch angles for a rocket system.
#Implement custom algorithms for calculating sqrt of a number using taylor series, compute inverse sine function, model the launch angle for a rocket to reach it's desired #altitude and analyze the launch angle range.

# project tree: 

#goph419lab01/

├── examples/

│   └── driver.py

├── figures/
│   
├── src/

│   └── goph419lab01/

│       └── functions.py

├── tests/

│   └── tests.py




#before installation, user should have everything set up including installing git and python (must be >=3.6). See lab 0 for more help. 

# installation process

#clone the repository,
#get into project root,
#create and activate the virtual environment

'''bash

git clone https://github.com/allisonu0630/goph419lab01.git


cd goph419lab01


python -m venv envlab1

envlab1\Scripts\activate

python -m pip install -r requirements.txt

# to calc launch angles and create plots
''' bash


$env:PYTHONPATH="src"          #this is so someone can run the driver code from a different machine


python examples/driver.py

# to test against NumPy
 

'''bash

python -m tests.tests

#complete!

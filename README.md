# Smidig_Prosjekt
## Download and install

Because of dependencies, these are the modules and versions which will be needed to run the GUI.

## Downloading Python
1. Download and use the newest version of python, which will be Python 3.12.3 64-bit. Use this link or download through Microsoft store
link: https://www.python.org/downloads/ 
2. Ensure you can run pip from the command line: python -m pip --version (NOT the same command for mac/linux) | MAC/Linux: python3 -m ensurepip --default-pip.
3. Ensure pip, setuptools, and wheel are up to date: python -m pip install --upgrade pip setuptools wheel | Unix/macOS: python3 -m pip install --upgrade pip setuptools wheel
4. Upgrade python packages if needed or using outdated versions, Windows: python -m pip install --upgrade "SomeProject" | Unix/macOS: python3 -m pip install --upgrade "SomeProject".

NOTE!! This has only been tested on the IDE VScode / Visual Studio Code.
source: https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-packages

## Downloading dependencies 
1. Open the project in an IDE (preferable on VScode), navigate to the 'artifacts' folder and open the IDE terminal. 
2. In the terminal, write these commands: 
        - pip install requests 
        - pip install flask 


## How to start the GUI Artifacts
1. Select a python intepreter, your IDE will suggest some python intepreters depending on your python version. Make sure you always select an intepreter with the newest version of python and it says global or recommended. We suggest not to use a virtual enviroment intepreter (venv), since it may cause some issues regarding dependencies. 
2. When an intepreter is selected, navigate to the 'Backend' folder from the 'artifacts' folder using the IDE terminal.
3. In the 'Backend' folder, start the appMain.py file using this command: python appMain.py 
4. It should indicate in the terminal that you are hosting a local server. It's purpose is to communicate with the API / vol.py file and collect the data from a volatility scan. 
5. Next step is to navigate back to the 'artifacts' folder using the IDE terminal. From there navgiate to the 'Fronted' folder.
6. In the 'Frontend' folder, start the appFrontMain.py using this command: python appFrontMain.py
7. If everything is downloaded correctly and you are using a non virtual enviroment intepreter, the GUI should start up!

## Quick guide on using the Artifacts (GUI)
1. Select an image file.
2. Choose a platform, ensure it matches the one used for the memory image file dump.
3. Select a Scan.
4. Click scan.


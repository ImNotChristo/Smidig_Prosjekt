# Smidig_Prosjekt
## Download Python and other dependencies

Because of dependencies, this are the modules and versions which will be needed to run the GUI.

### Downloading Python
1. Download and use the newest version of python, which will be Python 3.12.3 64-bit
link: https://www.python.org/downloads/ 
2. Ensure you can run pip from the command line: py -m pip --version (NOT the same command for mac/linux) | MAC/Linux: python3 -m ensurepip --default-pip.
3. Ensure pip, setuptools, and wheel are up to date: py -m pip install --upgrade pip setuptools wheel | Unix/macOS: python3 -m pip install --upgrade pip setuptools wheel
4. Upgrade python packages if needed or using outdated versions, Windows: py -m pip install --upgrade "SomeProject" | Unix/macOS: python3 -m pip install --upgrade "SomeProject".

NOTE!! This has only been tested on the IDE VScode / Visual Studio Code.
source: https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-packages

### Downloading dependencies 
1. Open the project in an IDE (preferable on VScode), navigate to the artifacts folder and open the IDE terminal. 
2. In the terminal, write these commands: 
        - pip install requests 
        - pip install flask 


# How to start the GUI Artifacts
1. Select a python intepreter, your IDE will suggest some python intepreters depending on your python version. Make sure you always selecting a intepreter with the newest version of python and it says global or recommended. We suggest to not use a virtual enviroment intepreter (venv), since it may cause some issues regarding dependencies. 
2. When an intepreter is selected, navigate to the Backend folder from the artifacts folder using the IDE terminal.
3. In the Backend folder, start the appMain.py file by writing this command: python appMain.py 
4. It should indicate in the terminal that you are hosting a local server. It's purpose is to communicate with the API / vol.py file and collect the data from a volatility scan. 
5. Next step is to navigate back to the artifacts folder using the IDE terminal. From there navgiate to the Fronted folder.
6. In the Frontend folder, start the appFrontMain.py using this command: python appFrontMain.py
7. If everything is downloaded correctly and you are using a non virtual enviroment intepreter, the GUI should start up!

For More information on how to use the GUI, read this documentation!
Link: bffgdfgsdfdfdf

# Alternativ
## Requirements

Volatility 3 requires Python 3.7.0 or later. To install the most minimal set of dependencies (some plugins will not work) use a command such as:

```shell
pip3 install -r requirements-minimal.txt
```

Alternately, the minimal packages will be installed automatically when Volatility 3 is installed using setup.py. However, as noted in the Quick Start section below, Volatility 3 does not *need* to be installed via setup.py prior to using it.

```shell
python3 setup.py build 
python3 setup.py install
```

To enable the full range of Volatility 3 functionality, use a command like the one below. For partial functionality, comment out any unnecessary packages in [requirements.txt](requirements.txt) prior to running the command.

```shell
pip3 install -r requirements.txt
```


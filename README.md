# Smidig_Prosjekt

Because of dependencies, this are the librarys and versions which will be needed to run the GUI.

1. Use the newest version of python, which will be Python 3.12.3 64-bit
link: https://www.python.org/downloads/ 
2. Ensure you can run pip from the command line: py -m pip --version (NOT the same command for mac/linux) | MAC/Linux: python3 -m ensurepip --default-pip.
3. Ensure pip, setuptools, and wheel are up to date: py -m pip install --upgrade pip setuptools wheel | Unix/macOS: python3 -m pip install --upgrade pip setuptools wheel
4. Install pillow, Windows: py -m pip install pillow | Unix/macOS: python3 -m pip install pillow.
5. Upgrade python packages if needed or using outdated versions, Windows: py -m pip install --upgrade "SomeProject" | Unix/macOS: python3 -m pip install --upgrade "SomeProject".
6. Use a IDE like VScode, but 

source: https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-packages

# How to use the first draft
1. Run the terminal file to make the program run.
2. 

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


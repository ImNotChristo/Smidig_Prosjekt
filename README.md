# Artifacts

Artifacts is a graphical user interface designed for the memory forensics tool, Volatility 3. This application aims to streamline the forensic analysis process by saving time, enhancing the ease of analyzing data from Volatility 3, and providing updated, user-friendly visual representations of the information. With Artifacts, users can more efficiently navigate and interpret the complex data involved in memory forensics, making it an invaluable tool for investigators and analysts.

## Extra Information

Due to dependencies, you must follow all the required steps to run the GUI successfully.

## Downloading Python
1. Download and install the latest version of Python, specifically Python 3.12.3 64-bit. You can use [this link](https://www.python.org/downloads/) or download it through the Microsoft Store (recommended).
2. Ensure you can run pip from the command line: 
   - Windows: `python -m pip --version`
   - macOS/Linux: `python3 -m ensurepip --default-pip`
3. Update pip, setuptools, and wheel: 
   - Windows: `python -m pip install --upgrade pip setuptools wheel`
   - macOS/Linux: `python3 -m pip install --upgrade pip setuptools wheel`
4. Upgrade Python packages if needed or if using outdated versions:
   - Windows: `python -m pip install --upgrade "SomeProject"`
   - macOS/Linux: `python3 -m pip install --upgrade "SomeProject"`

**Note:** This has only been tested on the IDE VSCode / Visual Studio Code. [Source](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-packages).

## Downloading Dependencies
1. Open the project in an IDE (preferably VSCode), navigate to the 'artifacts' folder, and open the IDE terminal.
2. In the terminal, run the following commands: 
   - `pip install requests`
   - `pip install flask`

## How to Start the Artifacts GUI
1. Select a Python interpreter. Your IDE will suggest some Python interpreters based on your Python version. Always select an interpreter with the latest version of Python and labeled as global or recommended. Avoid using a virtual environment interpreter (venv), as it may cause dependency issues.
2. Once an interpreter is selected, navigate to the 'Backend' folder from the 'artifacts' folder using the IDE terminal.
3. In the 'Backend' folder, start the `appMain.py` file using this command: `python appMain.py`
4. The terminal should indicate that you are hosting a local server. Its purpose is to communicate with the API/vol.py file and collect data from a Volatility scan.
5. Next, navigate back to the 'artifacts' folder using the IDE terminal. From there, navigate to the 'Frontend' folder.
6. In the 'Frontend' folder, start the `appFrontMain.py` file using this command: `python appFrontMain.py`
7. If everything is downloaded correctly and you are using a non-virtual environment interpreter, the GUI should start up!

## Quick Guide to Using Artifacts (GUI)
1. Select an image file.
2. Choose a platform, ensuring it matches the one used for the memory image file dump.
3. Select a scan.
4. Click scan.


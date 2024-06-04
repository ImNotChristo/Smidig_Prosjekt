import os
import subprocess

from flask import Flask, request, jsonify
import volatility3.plugins.windows.pslist as pslist
import volatility3.plugins.windows.cmdline as cmdline
from volatility3.framework import contexts, layers, automagic, exceptions
import json

appMain = Flask(__name__)


@appMain.route('/api/scan', methods=['POST'])
def scan_file():
    print("helloworld")
    data = request.get_json()
    print(data)
    filePath = data.get('FilePath')
    oSystem = data.get('OS')
    command = data.get('Command')

    # Absolute path to vol.py (adjust this to your actual path)
    volatility_path = "/Users/stefanspasenic/PycharmProjects/SmidiProject/volatility3/vol.py"

    # Check if the file path exists
    if not os.path.exists(filePath):
        return jsonify({"error": "File path does not exist"}), 400

    # Construct the command
    cmd = ["python3", volatility_path, "-f", filePath, f"{oSystem}.{command}"]

    # Print the command for debugging
    print("Executing command:", " ".join(cmd))

    try:
        # Execute the command
        terminalResult = subprocess.run(
            cmd,
            capture_output=True, text=True, check=True
        )

        # Print the output for debugging
        print("Command output:", terminalResult.stdout)
        print("Command error:", terminalResult.stderr)

        # Return the result as JSON
        return jsonify({
            "message": "Scan completed",
            "output": terminalResult.stdout,
            "error": terminalResult.stderr
        }), 200

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return jsonify({"error": f"Command execution failed: {e}"}), 500


@appMain.route('/api/dummydata2', methods=['GET'])
def get_dummy_data():
    # Load the JSON data from the file
    with open('/Users/stefanspasenic/PycharmProjects/SmidiProject/artifacts/Backend/dummyData.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)
    # get a link to this place (absolute link to appMain.py)   then ../../volatility3/vol.py    STORE IT IN scriptVol


# if not filepath # check if filepath is exists

## terminalResult = subprocess.run(
# HERE IS THE ARGUMENT AS YOU WOULD WRITE IT IN TERMINAL FOLLOWING LIKE THI S:
#   Pyhthon3 vol.py -f pathTODUMP OPERATINGSYSTEM.<command you choose for expl .info .psscan>


## []
#this is for the terminal to bring back the info , chat it ...
## capture_output = True, text=True, check= True


#)


## print(filePath)
## print("HEllo")

## return jsonify({"message": "Scan initiated", "File path": filePath}), 200

##@appMain.route('/api/dummydata2', methods=['GET'])
def get_dummy_data():
    # Load the JSON data from the file
    with open('/Users/stefanspasenic/PycharmProjects/SmidiProject/artifacts/Backend/dummyData.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)


# @appMain.route('/api/dummydata', methods=['GET'])
#def get_dummy_data():
#    # Hardcoded JSON data as a string
#    dummy_data = """
#    [
#        {
#            "id": 1,
#            "title": "First Item",
#            "link": "http://example.com/1"
#        },
#        {
#            "id": 2,
#            "title": "Second Item",
#            "link": "http://example.com/2"
#        },
#        {
#            "id": 3,
#            "title": "Third Item",
#            "link": "http://example.com/3"
#        }
#    ]
#    """
#    # Convert the string to a JSON object
#    data = jsonify(eval(dummy_data))
#    return data
#

@appMain.route('/')
def home():
    return "Welcome to the flask app!"


@appMain.route('/api/scan2', methods=['POST'])
def scan_memory_image():
    # This is where you will handle your Volatility 3 scanning logic
    data = request.get_json()
    memory_image_path = data.get('memory_image_path')

    # Placeholder for Volatility 3 scanning logic
    # You can call your Volatility 3 functions here and return the results
    result = {"message": "Scanning not implemented yet", "memory_image_path": memory_image_path}

    # return jsonify(result)
    return result


if __name__ == "__main__":
    appMain.run(port=6000)
    print("SERVER STARTED UP")

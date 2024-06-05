import os
import subprocess
from flask import Flask, request, jsonify
import json

appMain = Flask(__name__)

@appMain.route('/api/scan', methods=['POST'])
def scan_file():
    data = request.get_json()
    filePath = data.get('FilePath')
    command = data.get('Command')

    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to vol.py relative to the current script
    volatility_path = os.path.join(current_dir, '..', '..', 'volatility3', 'vol.py')

    if not os.path.exists(filePath):
        return jsonify({"error": "File path does not exist"}), 400

    cmd = ["python3", volatility_path, "-f", filePath, command]
    print("Executing command:", " ".join(cmd))

    try:
        terminalResult = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return jsonify({
            "message": "Scan completed",
            "output": terminalResult.stdout,
            "error": terminalResult.stderr
        }), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Command execution failed: {e}"}), 500

@appMain.route('/api/dummydata', methods=['GET'])
def get_dummy_data():
    with open(os.path.join(os.path.dirname(__file__), 'dummyData.json'), 'r') as file:
        data = json.load(file)
    return jsonify(data)

@appMain.route('/')
def home():
    return "Welcome to the flask app!"

if __name__ == "__main__":
    appMain.run(port=6000)

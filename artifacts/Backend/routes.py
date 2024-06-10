import os
import subprocess
from flask import request, jsonify
import json

"""
routes.py

This file defines and registers the routes for the Flask application.
It includes endpoints for scanning files and retrieving dummy data.
"""

def register_routes(app):
    
    @app.route('/api/scan', methods=['POST'])
    def scan_file():
        """
        Endpoint to scan a file using a specified command.
        Expects JSON with 'FilePath' and 'Command'.
        """
        data = request.get_json()  # Parse JSON data from request
        filePath = data.get('FilePath')
        command = data.get('Command')

        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to vol.py relative to the current script
        volatility_path = os.path.join(current_dir, '..', '..', 'volatility3', 'vol.py')

        # Check if the file path exists
        if not os.path.exists(filePath):
            return jsonify({"error": "File path does not exist"}), 400

        # Construct the command to be executed
        cmd = ["python3", volatility_path, "-f", filePath, command]
        print("Executing command:", " ".join(cmd))

        try:
            # Run the command and capture the output
            terminalResult = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return jsonify({
                "message": "Scan completed",
                "output": terminalResult.stdout,
                "error": terminalResult.stderr
            }), 200
        except subprocess.CalledProcessError as e:
            # Handle errors during command execution
            return jsonify({"error": f"Command execution failed: {e}"}), 500

    @app.route('/api/dummydata', methods=['GET'])
    def get_dummy_data():
        """
        Endpoint to get dummy data from a JSON file.
        """
        # Open and read the dummy data file
        with open(os.path.join(os.path.dirname(__file__), 'dummyData.json'), 'r') as file:
            data = json.load(file)
        return jsonify(data)

    @app.route('/')
    def home():
        """
        Home route for the Flask application.
        """
        return "Welcome to the flask app!"


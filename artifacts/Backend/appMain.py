from flask import Flask
from routes import register_routes

"""
appMain.py

This file initializes and runs the Flask application.
It imports and registers routes from the routes module.
"""

# Initialize the Flask application
appMain = Flask(__name__)

# Register routes from the routes module
register_routes(appMain)

# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    appMain.run(port=6000)

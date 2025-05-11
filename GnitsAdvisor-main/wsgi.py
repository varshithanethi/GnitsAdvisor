import sys
import os

# Add your project directory to Python path
path = '/home/varshithaa/mysite'
if path not in sys.path:
    sys.path.append(path)

# Import Flask app - update to match PythonAnywhere's expected path
from flask_app import app as application

# Configure logging
import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

if __name__ == "__main__":
    application.run()
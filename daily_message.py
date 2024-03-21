"""Entry point of application"""

from flask import Flask

# Create Flask app
app = Flask(__name__)

# # Configuration from config.py
from src.config import *

# All routes
from src.routes import *

if __name__ == '__main__':
		app.run(debug=True, port=5000)
	
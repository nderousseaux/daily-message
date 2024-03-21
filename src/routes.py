""" All routes of the application """

from daily_message import app

@app.route('/')
def index():
		return "Hello, World!"

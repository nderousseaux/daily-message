""" All routes of the application """

from daily_message import app
from src.bdd_utils import *
from src.midjourney_utils import *

@app.route('/')
def index():
	# Check if the image is already selected today
	if is_today_date():
		# If yes, return the image used today
		url = get_image_used_today()

		return url

	# If not, select a new image
	else:
		# Save all images in a file
		save_all_urls()

		# Select a random image
		url = get_random_unused_image()

		# Save the image used today
		save_image_used_today(url)

		# Return the image
		return url
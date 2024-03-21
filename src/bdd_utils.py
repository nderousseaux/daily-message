""" Functions for csv bdd.

IMG_BDD: the csv file that contains the images.
Two columns: url and use.
- url: the url of the image.
- use: the use of the image.

META_BDD: the meta file that contains the meta data.
First line: last call date.
Second line: url of image used today.
"""

import csv
import datetime
import random

IMG_BDD = "bdd.csv"
META_BDD = "meta.txt"

def create_meta():
	""" Create a meta file with the last call date """
	with open(META_BDD, "w") as f:
		f.write("x\n")
		f.write("x\n")


def is_today_date():
	""" Check if the last call date is today """

	# If META_BDD does not exist, create it
	try:
		with open(META_BDD, "r") as f:
			pass
	except FileNotFoundError:
		create_meta()

	# Check if the last call date is today
	with open(META_BDD, "r") as f:
		lines = f.readlines()
		if lines[0][:-1] == str(datetime.date.today()):
			return True
		else:
			return False

def save_image_used_today(url):
	""" Save the image used today """

	# If META_BDD does not exist, create it
	try:
		with open(META_BDD, "r") as f:
			pass
	except FileNotFoundError:
		create_meta()

	# Save the image used today
	with open(META_BDD, "w") as f:
		f.write(str(datetime.date.today()) + "\n")
		f.write(url + "\n")


def get_image_used_today():
	""" Return the image used today """

	# If META_BDD does not exist, create it
	try:
		with open(META_BDD, "r") as f:
			pass
	except FileNotFoundError:
		create_meta()

	# Return the image used today
	with open(META_BDD, "r") as f:
		lines = f.readlines()
		return lines[1]


def create_csv():
	""" Create a csv file with two columns: url and use """
	with open(IMG_BDD, "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerow(["url", "use"])


def add_to_csv(urls):
	""" Add multiples row to the csv file if it does not exist"""

	# If IMG_BDD does not exist, create it
	try:
		with open(IMG_BDD, "r") as f:
			pass
	except FileNotFoundError:
		create_csv()
	
	# Add the urls to the csv file if they are not already in
	with open(IMG_BDD, "r") as f:
		reader = csv.reader(f)
		data = list(reader)
		to_add = []
		for url in urls:
			if url not in [row[0] for row in data]:
				to_add.append([url, "unused"])

	with open(IMG_BDD, "a", newline="") as f:
		writer = csv.writer(f)
		for row in to_add:
			writer.writerow(row)
			
	
	
def mark_as_used(url):
	""" Mark the image as used """
	
	with open(IMG_BDD, "r") as f:
		reader = csv.reader(f)
		data = list(reader)
		for row in data:
			if row[0] == url:
				row[1] = "used"
	
	with open(IMG_BDD, "w", newline="") as f:
		writer = csv.writer(f)
		for row in data:
			writer.writerow(row)


def get_random_unused_image():
	""" Return a random unused image and mark it as used """
	
	# Get all unused images
	with open(IMG_BDD, "r") as f:
		reader = csv.reader(f)
		data = list(reader)
		unused = [row for row in data if row[1] == "unused"]

	# Select a random image
	url = random.choice(unused)[0]

	# Mark the image as used
	mark_as_used(url)

	return url

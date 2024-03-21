""" Functions for midjourney """

from selenium import webdriver

from src.bdd_utils import add_to_csv

MIDJOURNEY_URL = "https://www.midjourney.com/showcase"

def save_all_urls():
	""" Save all urls in a file """

	urls = get_all_images()

	add_to_csv(urls)


def get_all_images():
	"""Return all address of images from the feed page"""

	driver = webdriver.Chrome()
	driver.implicitly_wait(100)
	driver.maximize_window()
	driver.get(MIDJOURNEY_URL)
	driver.implicitly_wait(100)

	# Get url of all images (webp) (tag a, with style : image-set(url(...)))
	images = driver.find_elements_by_css_selector("a[style*='image-set']")
	urls = [image.get_attribute("style").split("url(")[1].split(")")[0] for image in images]

	driver.quit()

	# On remplace tout les 384_N.webp par 640_N.webp
	urls = [url.replace("384_N.webp", "640_N.webp") for url in urls]

	# On enlève les guillemets de trops
	urls = [url.replace('"', "") for url in urls]

	return urls



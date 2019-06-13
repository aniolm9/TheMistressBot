import os
import sys
import json
import requests
import urllib.request
try:
    from settings_secret import *
except:
    sys.exit("Missing settings_secret.py file.")

def getCineRipoll():
    # Get the HTML file.
    url = 'http://circusa.com/ca/ripoll/'
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
    html = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read().decode('utf-8')

    # Convert the HTML to an image.
    post_request = requests.post("https://hcti.io/v1/image", data={'html': html}, auth=(USER_ID, API_KEY))
    image_url = post_request.json()["url"] + ".png"

    # Download the image.
    image_request = urllib.request.urlopen(urllib.request.Request(image_url, headers=headers))
    image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imatges/cineripoll.png")
    f = open(image_file, "wb+")
    f.write(image_request.read())
    f.close()

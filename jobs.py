import os
import requests
import json
import urllib.request

def getCineRipoll():
    # Get the HTML file.
    url = 'http://circusa.com/ca/ripoll/'
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
    html = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read().decode('utf-8')

    # Convert the HTML to an image.
    user_id = ""
    api_key = ""
    post_request = requests.post("https://hcti.io/v1/image", data={'html': html}, auth=(user_id, api_key))
    image_url = post_request.json()["url"] + ".png"

    # Download the image.
    image_request = urllib.request.urlopen(urllib.request.Request(image_url, headers=headers))
    image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imatges/cineripoll.png")
    f = open(image_file, "wb+")
    f.write(image_request.read())
    f.close()

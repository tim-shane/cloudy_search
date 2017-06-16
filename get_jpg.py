from py_ms_cognitive import PyMsCognitiveImageSearch
import requests
from PIL import Image
from io import BytesIO

#This is a MS Cognitive Search v7.0 API
api = 'API-KEY'
'''
Switching to the v7 api because v5 returns the img URL wrapped in a bing.com url
'''
PyMsCognitiveImageSearch.SEARCH_IMAGE_BASE = 'https://api.cognitive.microsoft.com/bing/v7.0/images/search'

def return_img(search_term, search_modifier):
    search = search_term + ' ' + search_modifier
    print(search)
    bing_image = PyMsCognitiveImageSearch(api, search)
    results = bing_image.search()
    for i, result in enumerate(results):
        print(result.host_page_url)
        try:
            if result.content_url[-3:] == 'jpg':
                response = requests.get(result.content_url)
                image = Image.open(BytesIO(response.content))
                return image
        except ConnectionError:
            print("Could not download the image.")
            continue

from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
from py_ms_cognitive import PyMsCognitiveWebSearch, PyMsCognitiveImageSearch
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np


class CloudySearch(object):

    def __init__(self, api, search_term, search_modifier=""):
        """
        :param api: Bing v7.0 api key
        :param search_term: This is the basis for the web and image search.
        :param search_modifier:  This allows you to alter the image returned without modifying the web search.
          A good example would be adding 'vector' to your search to make a more pleasing word cloud image without making
          the words all about vector art or stock photo sites.
        :return: 
        """
        self.api = api
        self.search_term = search_term
        self.search_modifier = search_modifier

    def create_cloud(self):
        # Return Bing search snippets
        text = self.return_txt()

        # Get mask image from Bing
        image_mask = np.array(self.return_img())

        # potential feature
        stopwords = set(STOPWORDS)
        # stopwords.add(search_modifier)

        wordcloud = WordCloud(background_color="white", mask=image_mask, stopwords=stopwords)
        wordcloud.generate(text)

        image_colors = ImageColorGenerator(image_mask)
        plt.imshow(image_mask, cmap=plt.cm.gray, interpolation="None")
        plt.imshow(wordcloud.recolor(color_func=image_colors), alpha=.8, interpolation='None')
        plt.axis("off")
        return plt

    def return_txt(self):
        # Changing to v7 so you only need one API key.
        PyMsCognitiveWebSearch.SEARCH_WEB_BASE = \
            'https://api.cognitive.microsoft.com/bing/v7.0/search'

        bing_txt = PyMsCognitiveWebSearch(self.api, self.search_term)
        first_result = bing_txt.search()
        txt = str([snip.snippet for snip in first_result])
        return txt

    def return_img(self):

        """
        Switching to the v7 api because v5 returns 
        the img URL wrapped in a bing.com url
        """
        PyMsCognitiveImageSearch.SEARCH_IMAGE_BASE = \
            'https://api.cognitive.microsoft.com/bing/v7.0/images/search'
        search = self.search_term + ' ' + self.search_modifier
        bing_image = PyMsCognitiveImageSearch(self.api, search)
        results = bing_image.search()
        # todo If the image is unavailable, everything fails
        for i, result in enumerate(results):
            try:
                if result.content_url[-3:] == 'jpg':
                    response = requests.get(result.content_url)
                    image = Image.open(BytesIO(response.content))
                    return image
            except ConnectionError:
                print("Could not download the image.")
                continue

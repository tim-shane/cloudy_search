from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
from get_txt import return_txt
from get_jpg import return_img
import matplotlib.pyplot as plt
import numpy as np



def make_it_rain(search_term, search_modifier=""):

    # Return Bing search snippets
    text = return_txt(search_term)

    # Get mask image from Bing
    image_mask = np.array(return_img(search_term, search_modifier))

    # potential feature
    stopwords = set(STOPWORDS)
    # stopwords.add(search_modifier)

    wordcloud = WordCloud(background_color="white", mask=image_mask, stopwords=stopwords)
    wordcloud.generate(text)

    image_colors = ImageColorGenerator(image_mask)
    plt.imshow(image_mask, cmap=plt.cm.gray, interpolation="None")
    plt.imshow(wordcloud.recolor(color_func=image_colors), alpha=.8, interpolation='None')
    plt.axis("off")
    plt.show()

make_it_rain("tyrannosaurus rex")

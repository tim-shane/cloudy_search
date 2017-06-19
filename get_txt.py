from py_ms_cognitive import PyMsCognitiveWebSearch


# Changing to v7 so you only need one API key.
PyMsCognitiveWebSearch.SEARCH_WEB_BASE = 'https://api.cognitive.microsoft.com/bing/v7.0/search'

def return_txt(api, search_term):
    bing_txt = PyMsCognitiveWebSearch(api, search_term)
    first_result = bing_txt.search()
    txt = str([snip.snippet for snip in first_result])
    return txt

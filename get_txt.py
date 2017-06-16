from py_ms_cognitive import PyMsCognitiveWebSearch

#This is a MS Cognitive Search V.5 API
api = 'API-KEY'


def return_txt(search_term):
    txt = ""
    bing_txt = PyMsCognitiveWebSearch(api, search_term)
    first_result = bing_txt.search()
    snippets = []
    snippets.append([snip.snippet for snip in first_result])
    for word in snippets:
        txt += str(word)
    return txt

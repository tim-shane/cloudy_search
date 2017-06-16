from py_ms_cognitive import PyMsCognitiveWebSearch


api = '2943c57efabb48ddba07847b67f5ae5f'


def return_txt(search_term):
    txt = ""
    bing_txt = PyMsCognitiveWebSearch(api, search_term)
    first_result = bing_txt.search()
    snippets = []
    snippets.append([snip.snippet for snip in first_result])
    for word in snippets:
        txt += str(word)
    return txt

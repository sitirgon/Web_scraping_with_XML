from requests import get


class Page:
    def __init__(self):
        pass

    def get_page(self, url):
        r = get(url)
        r.encoding = 'UTF-8'
        return r

import requests
import lxml
from lxml import html


class Parser:
    def __init__(self, url, timeout=10):
        self.url = url
        self.timeout = timeout

    def get_tree(self):
        res = requests.get(self.url)
        tree = lxml.html.fromstring()
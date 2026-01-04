import requests as r
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import Optional

headers = { 'User-Agent' : 'Mozilla/5.0'}

def bs4crawl(url: str, method: str, selector: str, parser: str, encoding: Optional[str] = None):
    if method == 'get':
        response = r.get(url)
    elif method == 'post':
        response = r.get(url)
    
    if response.status_code == 200:
        html = response.text
        try:
            soup = BeautifulSoup(html, parser)
        except AttributeError as AE:
            raise AttributeError("parse 매개변수 오류")
        inner = soup.select(selector)
        return inner
    else: return Exception(response.status_code)
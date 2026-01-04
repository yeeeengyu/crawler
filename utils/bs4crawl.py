import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = { 'User-Agent' : 'Mozilla/5.0'}

def bs4crawl(url: str, method: str, headers: str, parse: str, encoding: str):
    response = requests.get()
from flask import Flask
from flask_restx import Api, Resource, fields
from utils.bs4crawl import bs4crawl
app = Flask(__name__)

api = Api(
    app,
    title = 'Crawler API',
    description= '크롤러 api'
); ns = api.namespace("crawl", description = 'asdf')


@app.route('/')
def health():
    return {"status":"ok"}

@app.route('/crawl/bs')
def crawl_bs(url: str, method: str, selector: str, parser: str, encoding: str):
    return bs4crawl(url, selector, parser, encoding)
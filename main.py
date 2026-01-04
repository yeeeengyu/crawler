from flask import Flask

app = Flask(__name__)

@app.route('/')
def health():
    return {"status":"ok"}

@app.route('/crawl/bs')
def crawl_bs(url: str, headers: str, parser: str, encoding: str):
    
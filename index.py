from flask import Flask, Response, redirect, __version__, jsonify
import requests

app = Flask(__name__)
source = 'https://github.com/zeit/now-examples/tree/master/python-flask'
css = '<link rel="stylesheet" href="/css/style.css" />'

@app.route('/')
def index():
    data = requests.get('https://currently-reads.now.sh/reading/29316435/json').json()
    simple_data = [{
        'title': book['book'][0]["title"][0],
        'image': book['book'][0]["image_url"][0],
        'started_at': book['started_at'][0],
        'read_at': book['read_at'][0],
        'date_added': book['date_added'][0],
        'rating': book['rating'][0],
        'url': book['book'][0]["link"][0],
        'description': book['book'][0]["description"][0],
        'author': book['book'][0]["authors"][0]["author"][0]["name"][0],
        'authors': [a["author"][0]["name"][0] for a in book['book'][0]["authors"]]
     } for book in data]
    return jsonify(simple_data)

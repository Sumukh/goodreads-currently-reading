from flask import Flask, Response, redirect, __version__, jsonify
import requests
from datetime import datetime, timedelta
import humanize

app = Flask(__name__)

def parse_goodreads_time(time_str):
    return datetime.strptime(time_str[0:-10] + time_str[-4:], '%a %b %d %H:%M:%S %Y')

def days_ago(time_str, cloak_recent=True):
    if not time_str:
        return ''
    if cloak_recent and (datetime.now() - parse_goodreads_time(time_str)) < timedelta(days=7):
        return 'this week'
    if cloak_recent and (datetime.now() - parse_goodreads_time(time_str)) < timedelta(days=31):
        return 'this month'
    if cloak_recent and (datetime.now() - parse_goodreads_time(time_str)) > timedelta(days=180):
        return 'a while ago'
    return humanize.naturaltime(datetime.now() - parse_goodreads_time(time_str))

def currently_reading(goodreads_user_id):
    data = requests.get('https://currently-reads.now.sh/reading/{}/json'.format(goodreads_user_id)).json()

    simple_data = [{
        'title': book['book'][0]["title"][0],
        'short_title': book['book'][0]["title"][0].split(':')[0],
        'image': book['book'][0]["image_url"][0],
        'started_at': book['started_at'][0],
        'started_at_ago': days_ago(book['started_at'][0]),
        'started_at_ago_actual': days_ago(book['started_at'][0], cloak_recent=False),
        'read_at': book['read_at'][0],
        'read_at_ago': days_ago(book['read_at'][0]),
        'read_at_ago_actual': days_ago(book['read_at'][0], cloak_recent=False),
        'read_count': book['read_count'][0],
        'date_added': book['date_added'][0],
        'date_added_ago': days_ago(book['date_added'][0]),
        'date_added_ago_actual': days_ago(book['date_added'][0], cloak_recent=False),
        'rating': book['rating'][0],
        'url': book['book'][0]["link"][0],
        'description': book['book'][0]["description"][0],
        'author': book['book'][0]["authors"][0]["author"][0]["name"][0],
        'authors': [a["author"][0]["name"][0] for a in book['book'][0]["authors"]]
    } for book in data]
    return simple_data

@app.route('/')
def index():
    return jsonify(currently_reading(29316435))

@app.route('/<userid>')
def currently_reading_user(userid):
    return jsonify(currently_reading(userid))

import os
import json
from datetime import datetime, timedelta

import humanize
import requests
import xmltodict

def get_shelf(user_id, shelf_name, page=1):
    api_key = os.getenv('GOODREADS_API_KEY')
    api_endpoint = 'https://www.goodreads.com/review/list/{}.xml?shelf={}&key={}&v=2&page={}'
    data = requests.get(api_endpoint.format(user_id, shelf_name, api_key, page))
    return json.loads(json.dumps(xmltodict.parse(data.text)))

def get_books(user_id, shelf_name='read'):
    data = get_shelf(user_id, shelf_name)
    # If you want the full data you'll need to paginate
    return data['GoodreadsResponse']['reviews']['review']

def parse_goodreads_time(time_str):
    if not time_str:
        return None
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


def goodreads_shelf(user_id, shelf_name, sort_by='date_added_parsed'):
    books = get_books(user_id, shelf_name)

    data = [{'title': book['book']["title"],
             'short_title': book['book']["title"].split(':')[0],
             'image': book['book']["image_url"],
             'num_pages': book.get('num_pages', 0),
             'rating': book['rating'],
             'started_at': book['started_at'],
             'started_at_parsed': parse_goodreads_time(book['started_at']),
             'started_at_ago': days_ago(book['started_at']),
             'started_at_ago_actual': days_ago(book['started_at'],
                                               cloak_recent=False),
             'read_at': book['read_at'],
             'read_at_parsed': parse_goodreads_time(book['read_at']),
             'read_at_ago': days_ago(book['read_at']),
             'read_at_ago_actual': days_ago(book['read_at'],
                                            cloak_recent=False),
             'read_count': book['read_count'],
             'date_added': book['date_added'],
             'date_added_parsed': parse_goodreads_time(book['date_added']),
             'date_added_ago': days_ago(book['date_added']),
             'date_added_ago_actual': days_ago(book['date_added'],
                                               cloak_recent=False),
             'url': book['book']["link"],
             'description': book['book']["description"],
             'author': book['book']["authors"]["author"]["name"],
             'authors': [book['book']["authors"]["author"]["name"]]
             # goodreads API bug lists only one author...
             } for book in books]
    return sorted(data, key=lambda b: (b[sort_by] or b['date_added_parsed'] or datetime(1980, 1, 1)), reverse=True)

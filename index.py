from flask import Flask, jsonify, redirect

from goodread_utils import goodreads_shelf

app = Flask(__name__)

@app.after_request
def add_header(response):
    # Add a five minute cache layer
    response.cache_control.max_age = 300
    return response

@app.route('/')
def index():
    return redirect('/29316435')

@app.route('/<int:user_id>')
def currently_reading_user(user_id):
    return jsonify(goodreads_shelf(user_id, 'currently-reading'))

@app.route('/<int:user_id>/read')
def past_reads_user(user_id):
    return jsonify(goodreads_shelf(user_id, 'read', sort_by='read_at_parsed'))

@app.route('/<int:user_id>/to-read')
def want_to_read(user_id):
    return jsonify(goodreads_shelf(user_id, 'to-read'))

@app.route('/<int:user_id>/shelf/<shelf>')
def user_shelf(user_id, shelf):
    return jsonify(goodreads_shelf(user_id, shelf))

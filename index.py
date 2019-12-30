from flask import Flask, jsonify, redirect, request

from goodread_utils import goodreads_shelf

app = Flask(__name__)

@app.after_request
def add_header(response):
    # Add a five minute cache layer
    response.cache_control.max_age = 300
    response.cache_control.public = True
    return response

@app.route('/')
def index():
    return redirect('/29316435')

@app.route('/<int:user_id>')
def currently_reading_user(user_id):
    full_fetch = request.args.get('full', False)
    return jsonify(goodreads_shelf(user_id, 'currently-reading',
                                   full_fetch=full_fetch))

@app.route('/<int:user_id>/read')
def past_reads_user(user_id):
    full_fetch = request.args.get('full', False)
    return jsonify(goodreads_shelf(user_id, 'read',
                                   sort_by='read_at_parsed', full_fetch=full_fetch))

@app.route('/<int:user_id>/to-read')
def want_to_read(user_id):
    full_fetch = request.args.get('full', False)
    return jsonify(goodreads_shelf(user_id, 'to-read', full_fetch=full_fetch))

@app.route('/<int:user_id>/shelf/<shelf>')
def user_shelf(user_id, shelf):
    full_fetch = request.args.get('full', False)
    return jsonify(goodreads_shelf(user_id, shelf, full_fetch=full_fetch))

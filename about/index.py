from flask import Flask, Response, __version__
app = Flask(__name__)
source = 'https://github.com/zeit/now-examples/tree/master/python-flask'
css = '<link rel="stylesheet" href="/css/style.css" />'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    name = path.upper()
    v = __version__
    return Response("%s<h1>%s</h1><ul><li>WSGI Enabled</li><li>Flask version <em>%s</em></li></ul><p>Visit the <a href='./'>home</a> page or view the <a href='%s'>source code</a>.</p>" % (css, name, v, source), mimetype='text/html')

#!/usr/bin/env python3
import os

from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

# Hook that runs before every request
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

# Home route
@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    status_code = 200   # Try changing this to 202 to see a different code
    headers = {}

    return make_response(response_body, status_code, headers)

# Extra route
@app.route('/hello')
def hello():
    return "<h1>Hello Flask!</h1>", 200

# Another example route that returns JSON
@app.route('/info')
def info():
    return {
        "host": request.headers.get("Host"),
        "app_name": current_app.name,
        "path": g.path
    }, 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)

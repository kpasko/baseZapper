from flask import Flask, send_from_directory

import os
import logging
from datetime import datetime
#from flask_cors import CORS
import time

logging.basicConfig(level=logging.INFO)

app = Flask(__name__, static_folder='static', static_url_path="/")
# CORS(app)

'''
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response
'''


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")


# local
if __name__ == '__main__':
    app.run()

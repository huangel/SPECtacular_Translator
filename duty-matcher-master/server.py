#!/usr/bin/python3

from flask import Flask, request, jsonify, send_file
from duties import get_match_results
from audio_new import main
import sys

app = Flask(__name__)


@app.route('/')
def index():
    index_file = 'www/index.html'
    return send_file(index_file)

@app.route('/scripts.js')
def js():
    js_file = 'www/scripts.js'
    return send_file(js_file)

@app.route('/', methods =['POST'])
def some_fx():
    text = request.form.get('textbox')

@app.route('/run', methods=['GET'])
def run():
    my_username = str(request.values.get('freshman-q')) if request.values.get('freshman-q') else 0
    my_lang = str(request.values.get('sophomore-q')) if request.values.get('sophomore-q') else 0
    other_username = str(request.values.get('junior-q')) if request.values.get('junior-q') else 0
    other_lang = str(request.values.get('senior-q')) if request.values.get('senior-q') else 0

    results = main(my_username, my_lang, other_username, other_lang)
    return jsonify({'results': results})

if __name__ == "__main__":
    # app.config['my_username'] = 'angel'
    # app.config['my_language'] = sys.argv[2]
    # app.config['other_username'] = sys.argv[3]
    # app.config['other_language'] = sys.argv[4]

    port = 5000
    app.run(host='0.0.0.0', port=port)

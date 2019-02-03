#!/usr/bin/python3

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS, cross_origin
from duties import get_match_results
from text_to_audio import main
from firebase import firebase
import sys

# firebase = firebase.FirebaseApplication('https://translation-bf31b.firebaseio.com', None)
# places_ref = firebase.collection()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    index_file = 'www2/index.html'
    return send_file(index_file)

@app.route('/www2/scripts.js')
def js():
    js_file = 'www2/scripts.js'
    return send_file(js_file)

@app.route('/', methods =['POST'])
def some_fx():
    text = request.form.get('textbox')

@app.route('/run', methods=['GET'])
@cross_origin()
def run():
    print("hello")
    my_username = str(request.values.get('freshman-q')) if request.values.get('freshman-q') else 0
    my_lang = str(request.values.get('sophomore-q')) if request.values.get('sophomore-q') else 0
    other_username = str(request.values.get('junior-q')) if request.values.get('junior-q') else 0
    other_lang = str(request.values.get('senior-q')) if request.values.get('senior-q') else 0
    print(my_username, my_lang, other_username, other_lang)
    print("run")
    main(my_username, my_lang, other_username, other_lang)
    print("ran")
    return jsonify({'results': "running"})

@app.route('/get_results', methods=['GET'])
@cross_origin()
def get_results():
    return jsonify({'results': "anything"})
if __name__ == "__main__":
    # app.config['my_username'] = 'angel'
    # app.config['my_language'] = sys.argv[2]
    # app.config['other_username'] = sys.argv[3]
    # app.config['other_language'] = sys.argv[4]

    port = 5050
    app.run(host='0.0.0.0', port=port, threaded = True)

from flask import Flask, request, render_template, redirect, url_for, jsonify
from datetime import date
import vas
from flask_cors import CORS
import cv
import requests
import mch_text
# import jsonify


app = Flask(__name__)
CORS(app, resource={r"/api/*":{"origin":"*"}})


@app.route('/')
def homes():
    return "Hello,cross-origin-world"

#keywords
@app.route('/image', methods=['POST'])
def text_result():
    text=request.get_json()['base64']
    resp = cv.getEmotion(text)
    return jsonify(resp.decode('UTF-8'))

@app.route('/result', methods=['POST'])
def result():
    text = request.get_json()['text']
    print(request.get_json())
    a=vas.get_vects(str(text))
    return jsonify(a)

if __name__ == "__main__":
    app.run(port=8000, debug=True)

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from flask import Flask, render_template, jsonify
from selenium_script.scraper import fetch_trending_topics
import pymongo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['GET'])
def run_script():
    result = fetch_trending_topics()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

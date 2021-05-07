from flask import Flask, jsonify, request
from flask_cors import CORS
import csv
from source_map import source_map

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# enable cors
CORS(app, resources={r'/*': {'origins': '*'}})

# load sources
sources = source_map('sources.csv')
sources.load_sources()

# sanity check
@app.route('/pong', methods=['GET'])
def pong_ping():
    return jsonify('Ping!')



# sanity check
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Pong!')

@app.route('/sources', methods=['GET'])
def source_list():
    bias = request.args.get('bias')
    return jsonify(sources.fetch_sources(int(bias)))


@app.route('/articles', methods=['POST'])
def api():
    data = request.get_json()
    bias = data['bias']
    source_list = data['sources']
    return jsonify(sources.fetch_articles(int(bias), source_list))


if __name__ == '__main__':
    app.run()

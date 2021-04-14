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
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Pong!')

@app.route('/api', methods=['GET'])
def api():
    bias = request.args.get('bias')
    return jsonify(sources.fetch_articles(int(bias)))


if __name__ == '__main__':
    app.run()

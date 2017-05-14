from flask import Flask, url_for, jsonify
from elasticsearch import Elasticsearch
from datetime import datetime
import os


import sys
if sys.version_info.major < 3:
    reload(sys)

es_host = os.environ['DOCKER_MACHINE_IP']
print('Elastic host is {}'.format(es_host))

# by default we don't sniff, ever
es = Elasticsearch([es_host])

app = Flask(__name__)


@app.route('/info')
def api_info():
    return jsonify(es.info())

@app.route('/health')
def api_health():
    return jsonify(es.cluster.health())

@app.route('/')
def api_root():
    return 'Welcome to the flask API with elasticsearch backend. Try /health endpoint'


@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


@app.route('/index/<id>')
def index_doc():
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="test-index", doc_type='tweet', id=id, body=doc)
    print(res['created'])
    es.indices.refresh(index="test-index")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

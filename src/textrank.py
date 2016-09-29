import urllib
from bs4 import BeautifulSoup
import nltk
import networkx as nx
import numpy as np
import json
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

from flask import Flask, request

from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

def get_html_document(url=''):
    print url

    html = urllib.urlopen(url).read()

    print html
    soup = BeautifulSoup(html, 'html.parser')

    # get text
    return soup.get_text()


@app.route('/rank', methods=['GET'])
@payment.required(100)
def textrank():
    url = request.args.get('url')

    document = get_html_document(url)

    if document == '':
        return 'Unable to fufill request, please try again later'

    sentence_tokenizer = PunktSentenceTokenizer()
    sentences = sentence_tokenizer.tokenize(text=document)

    bow_matrix = CountVectorizer().fit_transform(sentences)
    normalized = TfidfTransformer().fit_transform(bow_matrix)

    similarity_graph = normalized * normalized.T

    nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
    scores = nx.pagerank(nx_graph)

    return json.dumps(sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True))

if __name__ == '__main__':
    app.run(host='::')

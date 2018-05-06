from flask import jsonify
from nltk.tokenize.punkt import PunktSentenceTokenizer
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import networkx as nx


def textRankAlgorithmOld(document):
    sentence_tokenizer = PunktSentenceTokenizer()
    sentences = sentence_tokenizer.tokenize(document)

    bow_matrix = CountVectorizer().fit_transform(sentences)
    normalized = TfidfTransformer().fit_transform(bow_matrix)

    similarity_graph = normalized * normalized.T

    nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
    scores = nx.pagerank(nx_graph)
    return jsonify(sorted(((scores[i], s) for i, s in enumerate(sentences)),
                          reverse=True))

from flask import Flask, request
from flask_cors import CORS

from KeywordExtraction import keyword_extraction
from Tokenize import wordTokenize, sentanceTokenize, removeStopWords, stemming
from mindmap import mindmap
from summarization import textRankAlgorithm

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/wordtokenize", methods=["POST"])
def function1():
    data = request.json['data']
    return wordTokenize(data)


@app.route("/sentancetokenize", methods=["POST"])
def function2():
    data = request.json['data']
    return sentanceTokenize(data)


@app.route("/removestopwords", methods=["POST"])
def function3():
    data = request.json['data']
    return removeStopWords(data)


@app.route("/stemming", methods=["POST"])
def function4():
    data = request.json['data']
    return stemming(data)


@app.route("/summarizer", methods=["POST"])
def function5():
    data = request.json['data']
    return textRankAlgorithm(data)

@app.route("/mindmap", methods=["POST"])
def function6():
    data = request.json['data']
    return mindmap(data)

@app.route("/keywordextraction", methods=["POST"])
def function7():
    data = request.json['data']
    return keyword_extraction(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)

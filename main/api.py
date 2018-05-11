from flask import Flask, request, json
from flask_cors import CORS

from Database import login_user, user_signup
from KeywordExtraction import keyword_extraction
from Tokenize import wordTokenize, sentanceTokenize, removeStopWords, stemming
from mindmap import mindmap_generate
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
    return mindmap_generate(data)


@app.route("/keywordextraction", methods=["POST"])
def function7():
    data = request.json['data']
    return keyword_extraction(data)


@app.route("/login", methods=["POST"])
def function8():
    userName = request.json['userName']
    userPassword = request.json['userPassword']
    return login_user(userName, userPassword)


@app.route("/signup", methods=["POST"])
def function9():
    userName = request.json['userName']
    userPassword = request.json['userPassword']
    userEmail = request.json['userEmail']
    return user_signup(userName, userPassword, userEmail)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)

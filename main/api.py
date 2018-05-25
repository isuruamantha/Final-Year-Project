from flask import Flask, request, json
from flask_cors import CORS

from Database import login_user, user_signup, save_summary, history
from KeywordExtraction import keyword_extraction
from Tokenize import wordTokenize, sentanceTokenize, removeStopWords, stemming
from mindmap import mindmap_generate
from summarization import textrank_algorithm

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
    sentences_count = request.json['sentences_count']
    keyword_count = request.json['keyword_count']
    return textrank_algorithm(data, int(sentences_count))


@app.route("/mindmap", methods=["POST"])
def function6():
    data = request.json['data']
    sentences_count = request.json['sentences_count']
    keyword_count = request.json['keyword_count']
    return mindmap_generate(data, int(sentences_count), int(keyword_count))


@app.route("/keywordextraction", methods=["POST"])
def function7():
    data = request.json['data']
    sentences_count = request.json['sentences_count']
    keyword_count = request.json['keyword_count']
    return keyword_extraction(data, True, int(keyword_count), "keyword")


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


@app.route("/savesummary", methods=["POST"])
def function10():
    userId = request.json['userId']
    summary = request.json['summary']
    return save_summary(userId, summary)


@app.route("/history", methods=["POST"])
def function11():
    userId = request.json['userId']
    return history(userId)


@app.route("/keywordsforbarchart", methods=["POST"])
def function12():
    data = request.json['data']
    sentences_count = request.json['sentences_count']
    keyword_count = request.json['keyword_count']
    return keyword_extraction(data, True, int(keyword_count), "chart")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)

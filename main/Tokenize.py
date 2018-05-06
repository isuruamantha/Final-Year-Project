from flask import jsonify
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer


# To tokenize the words
def wordTokenize(data):
    tokenized_data = (word_tokenize(data))
    return jsonify(tokenized_data)


# To tokenize the sentances
def sentanceTokenize(data):
    tokenized_data = (sent_tokenize(data))
    return jsonify(tokenized_data)


# To remove the stop words in english language
def removeStopWords(data):
    stopWords = set(stopwords.words('english'))
    words = word_tokenize(data)
    wordsFiltered = []

    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)

    print(wordsFiltered)
    return jsonify(wordsFiltered)


# To stemming the words
def stemming(data):
    ps = PorterStemmer()
    words = word_tokenize(data)
    wordsStemmed = []

    for word in words:
        print(word + ":" + ps.stem(word))
    return jsonify(word)
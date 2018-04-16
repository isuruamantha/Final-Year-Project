import codecs
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import ngrams

# -*- coding: utf8 -*-

file_output_tokenize = codecs.open('tokens.txt', 'w', 'utf-16')
file_output_punctuation = codecs.open('punctuation.txt', 'w', 'utf-16')
file_output_stopwords = codecs.open('stopWords.txt', 'w', 'utf-16')

with codecs.open('para1.txt', 'r', 'utf-16') as sampleFile:
    data = sampleFile.read()

    ## tokenize into words
    tokenArray = []
    tokens = word_tokenize(data)

    for i in tokens:
        file_output_tokenize.write(i)
        file_output_tokenize.write(u"\r\n")
        tokenArray.append(i)
    file_output_tokenize.close()

    ## number replacement
    # Iterate through the string, replacing "0" for the digits
    for i in data:
        if i.isdigit():
            data = data.replace(i, "0")

        ## remove punctuation
    with codecs.open('tokens.txt', 'r', 'utf-16') as sampleFile:
        data = sampleFile.read()
    for c in string.punctuation:
        data = data.replace(c, "")
    file_output_punctuation.write(data)
file_output_punctuation.close()

## stop words removal
stopWords = set(stopwords.words("sinhala"))

print('{} {}'.format('token length before removing stop words :', len(tokens)))
for i in tokenArray:
    filtered_sentence = [w for w in tokenArray if not w in stopWords]
    # filtering the stop word list from the source text

    for i in filtered_sentence:
        file_output_stopwords.write(i)
        file_output_stopwords.write(u"\r\n")

print('{} {}'.format('token length after removing stop words :', len(filtered_sentence)))
file_output_stopwords.close()

## create n-grams
ngramArray = []
n = 3
with codecs.open('tokens.txt', 'r', 'utf-16') as sampleFile:
    data = sampleFile.read()
    trigrams = ngrams(data.split(), n)
    for grams in trigrams:
        ngramArray.append(grams)
    print('{} {}'.format('ngrams are :', ngramArray))

## synonym replacement
f = codecs.open('sample_synonyms.txt', 'r', 'utf_8')
x = f.read()
y = str(x).splitlines()
for i in y:
    string = str(i)
    words = string.split(',')
print(words)

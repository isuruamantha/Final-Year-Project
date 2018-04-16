import networkx as nx
import nltk, re
from collections import Counter
from nltk import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

stopwords_new = []
summed_sents = []
splited_words = []
orderedword_list = []


# Load the stopwords from the
def get_stopwords(stopwords):
    stopwords_list = nltk.word_tokenize(stopwords)
    for word in stopwords_list:
        if not word.isdigit():
            stopwords_new.append(word)


def count_words(split_words):
    count = Counter()
    for word in split_words:
        count[word] += 1
    return count


def remove_stopwords(split_sents, stop_word_list_new):
    summed_phrase = ''
    words = split_chapter(split_sents)
    for word in words:
        if word not in stop_word_list_new:
            summed_phrase = summed_phrase + word + ' '
            # summed_sents.append(word)
            ''''print('appended ' + word)
        else:
            print('removed ' + word)'''
    return summed_phrase


def sentence_splitter(full_text, sent_phrases):
    phrase_wo_stp = ''
    if full_text:
        sents_list = sent_tokenize(full_text)
        for sentence in sents_list:
            phrase_wo_stp = phrase_wo_stp + sentence + '\n'
        return phrase_wo_stp
    elif sent_phrases:
        return sent_phrases.split('\n')


def split_chapter(full_text):
    # splited_text = nltk.word_tokenize(full_text)
    splited_text = re.split('\n\n| \n|\n|[ ]|,', full_text)
    for word in splited_text:
        if not word == '':
            splited_words.append(word)
    return splited_words


def title_filter(splited_text):
    titles = []
    title_re = r"^[0-9].[0-9] "
    for sentence in splited_text:
        if re.search(title_re, sentence):
            print(sentence)
            titles.append(sentence)
    return titles


def textRankAlgorithm(document):
    # sentence_tokenizer = nltk.PunktSentenceTokenizer()
    # sentences = sentence_tokenizer.tokenize(document)

    bow_matrix = CountVectorizer().fit_transform(document)
    normalized = TfidfTransformer().fit_transform(bow_matrix)

    similarity_graph = normalized * normalized.T

    nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
    scores = nx.pagerank(nx_graph)
    print(scores)
    return print(sorted(((scores[i], s) for i, s in enumerate(document)),
                        reverse=True))


def main(filename):
    stopwords = open('StopWords_sin.txt', 'r', encoding='utf-16').read()
    full_text = open(filename, 'r', encoding='utf-16').read()
    splited_text = sentence_splitter([], full_text)
    title_list = title_filter(splited_text)
    get_stopwords(stopwords)
    # split_chapter(full_text)
    text_no_stp = remove_stopwords(full_text, stopwords_new)
    splited_sents = sentence_splitter(text_no_stp, [])
    textRankAlgorithm(splited_text);

    print('------------------------------------------------------')
    print(splited_sents)
    bins = count_words(splited_words)
    for key, value in bins.most_common():
        orderedword_list.append(key)
        # print(key, value)


main('unicodeChap1.txt')

# print(orderedword_list)

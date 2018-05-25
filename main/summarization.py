import io
from time import gmtime, strftime

import networkx as nx
import nltk, re
from collections import Counter

from flask import jsonify
from nltk import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from textrank import filter_for_tags, normalize, unique_everseen, buildGraph

stopwords_new = []


# Stemming words
def stemming_words(tokens_list):
    stem_dictionary_path = open('assets/suffixes.txt', 'r', encoding='utf-8').read()
    stemmed = []
    for token in tokens_list:
        word = token
        for suffix in stem_dictionary_path:
            if word.endswith(suffix):
                word = word.replace(suffix, "")
                break
        stemmed.append(word)
    return stemmed


# Load the stopwords from the
def get_stopwords(stopwords):
    stopwords_list = nltk.word_tokenize(stopwords)
    for word in stopwords_list:
        if not word.isdigit():
            stopwords_new.append(word)


# To count the words
def count_words(split_words):
    count = Counter()
    for word in split_words:
        count[word] += 1
    return count


# To remove the stop words from the given list
def remove_stopwords(split_sents, stop_word_list_new):
    summed_phrase = ''
    words = split_chapter(split_sents)
    for word in words:
        if word not in stop_word_list_new:
            summed_phrase = summed_phrase + word + ' '
    return summed_phrase


# To split the sentences
def sentence_splitter(full_text, sent_phrases):
    phrase_wo_stp = ''
    if full_text:
        sents_list = sent_tokenize(full_text)
        for sentence in sents_list:
            phrase_wo_stp = phrase_wo_stp + sentence + '\n'
        return phrase_wo_stp
    elif sent_phrases:
        return sent_phrases.split('\n')


# To split the chapters
def split_chapter(full_text):
    splited_words = []
    # splited_text = nltk.word_tokenize(full_text)
    splited_text = re.split('\n\n| \n|\n|[ ]|,', full_text)
    for word in splited_text:
        if not word == '':
            splited_words.append(word)
    return splited_words


# Main algorithm
def textrank_algorithm(document, sentence_count):
    full_text = document

    print('------------------------ Sentence Tokenizer ------------------------------')
    print()
    sentence_tokenizer_list = nltk.PunktSentenceTokenizer()
    initial_tokenized_sentences = sentence_tokenizer_list.tokenize(full_text)
    print(initial_tokenized_sentences)

    print('------------------------ Load stop words ------------------------------')
    print()
    stopwords = open('assets/StopWords_sin.txt', 'r', encoding='utf-16').read()
    get_stopwords(stopwords)
    print(stopwords_new)

    print('------------------------ Remove stop words ------------------------------')
    print()
    text_no_stp = remove_stopwords(full_text, stopwords_new)
    print(text_no_stp)

    print('------------------------ After removing stop words ------------------------------')
    print()
    splited_sents = sentence_splitter(text_no_stp, [])
    print(splited_sents)
    print()

    print('------------------------ Sentence tokenizer ------------------------------')
    print()
    sentence_tokenizer = nltk.PunktSentenceTokenizer()
    sentences = sentence_tokenizer.tokenize(splited_sents)
    print(sentences)

    print('------------------------ Stemming the words ------------------------------')
    print()
    print(stemming_words(splited_sents))

    print('------------------------ TextRank Algorithm ------------------------------')
    print()

    print('------------------------ Bow Matrix  ------------------------------')
    print()
    # Sparce matrix
    bow_matrix = CountVectorizer().fit_transform(sentences)
    # print(bow_matrix)

    print('------------------------ normalized Matrix  ------------------------------')
    print()
    normalized = TfidfTransformer().fit_transform(bow_matrix)
    # print(normalized)

    similarity_graph = normalized * normalized.T

    nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
    print(nx_graph)
    scores = nx.pagerank(nx_graph)

    sorted_sentences = sorted(scores, key=scores.get,
                              reverse=True)
    print(sorted_sentences)

    summary = ' '.join([initial_tokenized_sentences[i] for i in sorted_sentences][:sentence_count])

    print('------------------------ Generated Summary  ------------------------------')
    print()

    return (summary)


# For testing purposes
def mai():
    text = "තොරතුරු තාක්‍ෂණය දේශීයකරණය දැන්‌ සැම තැනම කතා කරන මාතෘකාවක්‌ වෙලා. පහුගිය කාලය තුළ Mozilla Firefox, ලිනක්‌ස්‌ මෙහෙයුම්‌ පද්‌ධති වගේම Microsoft Windows Vista සහ MS Office 2007 පැකේජයන්‌ පවා සිංහලට පැමිණීම මෙහිලා විශේෂ කොට දක්‌වන්‌න පුලුවන්‌. එමෙන්‌ම නුදුරු අනාගතයේදී තව තවත්‌ වටිනා මෘදුකාංග දේශීයකරණය වෙනු ඇති. ඉංග්‍රීසි මෘදුකාංග වලට සිංහල අතුරු මුහුණත්‌ (interface) සැකසීම දේශීයකරණයට ප්‍රමාණවත්‌ නොවේ, පරිශීලකයා අනුව ක්‍රියාකාරකම් හා පෙර ලැබූ පළපුරුද්ද එකතු කලයුතුය(පරිශීලන අත්දැකීම). අපගේ දැක්‌ම අනුව දේශීයකරණය දෙයාකාරයකින්‌ සිදුවිය යුතු යි. පළමුව දේශීය ඵලදායිතාව නැංවීම සඳහා අවශ්‍ය තොරතුරු තාක්‍ෂණය දැනුම ඉහල දැමිය යුතුය. ගොවිපලේ සිට කර්‌මාන්‌ත සහ කාර්‌යාලීය මට්‌ටම දක්‌වා තොරතුරු තාක්‍ෂණය භාවිතා කිරීමට ඇති හැකියාව වැඩි දියුණු කිරීම මේ යටතට වැටේ. භාෂාව මේ සඳහා විශාල බාධකයක්‌ විය හැකි බැවින්‌ දේශීයකරණයට සිදු කිරීමේදී ඒ ඒ අංශයන්‌ගෙන්‌ රටට සිදුව ඍජු සහ වක්‍ර බලපෑම්‌ අනුව ඒවාට ප්‍රමුඛතාවය ලබා දී ක්‍රියාත්‌මක කළ යුතුය. දෙවන කොටසට අයිති වනුයේ තොරතුරු තාක්‍ෂණය භාවිතා කිරීම සඳහා තාක්‍ෂණවේදීන්‌ සැකසීමේ කාර්‌යයයි. මේ සඳහා ක්‍රමවත්‌ අධ්‍යාපන ක්‍රමයක්‌ සැකසීම සහ ඒ සඳහා අවශ්‍ය පහසුකම්‌ ශිෂ්‍ය ශිෂ්‍යාවන්‌ට සහ දැනට එම ක්‍ෂේත්‍රෙය්‌ නියැලෙන අයට ලබාදීම අනිවාර්‌ය වේ. අ.පො.ස. සාමාන්‍ය පෙළ සහ උසස්‌ පෙළ සඳහා අතිරේක විෂයක්‌ ලෙස තොරතුරු තාක්‍ෂණය(ICT සහ GIT) හඳුන්‌වා දීම මෙහි ලා අගය කළ යුතු ක්‍රියාමාර්‌ගයකි. එසේම නව විෂය නිර්‌දේශය යටතේ උසස්‌ පෙළ ප්‍රධාන විෂයක්‌ ලෙස තොරතුරු තාක්‍ෂණය (IT) ඉගැන්‌වීමට ආරම්‌භ කිරීම වඩාත්‌ අගය කළ යුතුය. ඉතා වටිනා අගය කළයුතු විෂය නිර්‌දේශයකින්‌ එය සමන්‌විතය. අපගේ දැක්‌මට අනුව දැනට අරටුව ශක්‌තිමත්‌ව සැකසෙමින්‌ පවතී. අනෙකුත්‌ බාහිර කරුණු ද, එයට අවශ්‍ය කරන ශක්‌තිය ද ලබාදේ නම්‌ ත්‍රස්‌තවාදයෙන්‌ මිදුනු අපේ රටට අහිමිව ගිය ආර්‌ථික ස්‌ථානයද නැවත හිමිකරදීමට අනාගත පරපුරට හැකි වනු නොඅනුමානය."
    textrank_algorithm(text)

# mai()

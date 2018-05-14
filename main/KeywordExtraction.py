import re
import os
import operator
from time import strftime

import nltk
from flask import jsonify, make_response

debug = False
test = True
stopwords_new = []


def is_number(s):
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False


def separate_words(text, min_word_return_size):
    """
    Utility function to return a list of all words that are have a length greater than a specified number of characters.
    @param text The text that must be split in to words.
    @param min_word_return_size The minimum no of characters a word must have to be included.
    """
    splitter = re.compile('[^a-zA-Z0-9_\\+\\-/]')
    words = []
    for single_word in splitter.split(text):
        current_word = single_word.strip().lower()
        # leave numbers in phrase, but don't count as words, since they tend to invalidate scores of their phrases
        if len(current_word) > min_word_return_size and current_word != '' and not is_number(current_word):
            words.append(current_word)
    return words


def sentence_splitter(full_text, sent_phrases):
    phrase_wo_stp = ''
    if full_text:
        sents_list = nltk.sent_tokenize(full_text)
        for sentence in sents_list:
            phrase_wo_stp = phrase_wo_stp + sentence + '\n'
        return phrase_wo_stp
    elif sent_phrases:
        return sent_phrases.split('\n')


def build_stop_word_regex(stop_word_file_path):
    stopwords_new = []
    stop_word_list = open('StopWords_sin.txt', 'r', encoding='utf-16').read()

    stopwords_list = nltk.word_tokenize(stop_word_list)
    for word in stopwords_list:
        if not word.isdigit():
            stopwords_new.append(word)

    stop_word_regex_list = []
    for word in stopwords_new:
        word_regex = r'\b' + word + r'(?![\w-])'  # added look ahead for hyphen
        stop_word_regex_list.append(word_regex)
    stop_word_pattern = re.compile('|'.join(stop_word_regex_list), re.IGNORECASE)
    return stop_word_pattern


def generate_candidate_keywords(sentence_list, stopword_pattern):
    phrase_list = []
    for s in sentence_list:
        tmp = re.sub(stopword_pattern, '|', s.strip())
        phrases = tmp.split("|")
        for phrase in phrases:
            phrase = phrase.strip().lower()
            if phrase != "":
                phrase_list.append(phrase)
    return phrase_list


def split_chapter(full_text):
    splited_words = []
    # splited_text = nltk.word_tokenize(full_text)
    splited_text = re.split('\n\n| \n|\n|[ ]|,', full_text)
    for word in splited_text:
        if not word == '':
            splited_words.append(word)
    return splited_words


def remove_stopwords(split_sents, stop_word_list_new):
    summed_phrase = []
    words = split_chapter(split_sents)
    for word in words:
        if word not in stop_word_list_new:
            summed_phrase.append(word)
    return summed_phrase


# Load the stopwords from the
def get_stopwords(stopwords):
    stopwords_list = nltk.word_tokenize(stopwords)
    for word in stopwords_list:
        if not word.isdigit():
            stopwords_new.append(word)


def calculate_word_scores(phraseList):
    word_frequency = {}
    word_degree = {}
    for phrase in phraseList:
        # word_list = separate_words(phrase, 0)
        word_list_length = len(phrase)
        word_list_degree = word_list_length - 1
        # if word_list_degree > 3: word_list_degree = 3 #exp.
        # for word in phraseList:
        word_frequency.setdefault(phrase, 0)
        word_frequency[phrase] += 1
        word_degree.setdefault(phrase, 0)
        word_degree[phrase] += word_list_degree  # orig.
        # word_degree[word] += 1/(word_list_length*1.0) #exp.
    for item in word_frequency:
        word_degree[item] = word_degree[item] + word_frequency[item]

    # Calculate Word scores = deg(w)/frew(w)
    word_score = {}
    for item in word_frequency:
        word_score.setdefault(item, 0)
        word_score[item] = word_degree[item] / (word_frequency[item] * 1.0)  # orig.
    # word_score[item] = word_frequency[item]/(word_degree[item] * 1.0) #exp.
    return word_score


def generate_candidate_keyword_scores(phrase_list, word_score):
    keyword_candidates = {}
    for phrase in phrase_list:
        keyword_candidates.setdefault(phrase, 0)
        word_list = separate_words(phrase, 0)
        candidate_score = 0
        for word in word_list:
            candidate_score += word_score[word]
        keyword_candidates[phrase] = candidate_score
    return keyword_candidates


def filter_sorted_keywords(sorted_keywords):
    filterd_keyword_list = []
    for word in sorted_keywords:
        filterd_keyword_list.append(word[0])

    return keywords_json_formatter(filterd_keyword_list)


def filter_keywords(sorted_keywords):
    filterd_keyword_list = []
    for word in sorted_keywords:
        filterd_keyword_list.append(word[0])

    return filterd_keyword_list


def keywords_json_formatter(unformatted_text):
    topList = []

    for index, tex in enumerate(unformatted_text):
        tmpDict1 = {}
        tmpDict1["key"] = tex
        tmpDict1["value"] = index
        topList.append(tmpDict1)

    return (topList)


def keyword_extraction(sinhala_text, is_result_formatted, keyword_count):
    text = sinhala_text
    # text = "Sri Lanka's documented history spans 3,000 years, with evidence of pre-historic human settlements dating back to at least 125,000 years.[11] It has a rich cultural heritage and the first known Buddhist writings of Sri Lanka, the Pāli Canon, date back to the Fourth Buddhist council in 29 BC.[12][13] Its geographic location and deep harbours made it of great strategic importance from the time of the ancient Silk Road through to the modern Maritime Silk Road.[14][15][16] Sri Lanka was known from the beginning of British colonial rule as Ceylon (/sɪˈlɒn, seɪ-, siː-/). A nationalist political movement arose in the country in the early-20th century to obtain political independence, which was granted in 1948; the country became a republic and adopted its current name in 1972. Sri Lanka's recent history has been marred by a thirty-year civil war, which decisively ended when the Sri Lanka Armed Forces defeated the Liberation Tigers of Tamil Eelam (LTTE) in 2009.[17]"

    # Split text into sentences
    stopwords = open('StopWords_sin.txt', 'r', encoding='utf-16').read()
    print('------------------------ Load stop words k------------------------------')
    print()
    get_stopwords(stopwords)
    print(stopwords_new)
    print()
    # split_chapter(full_text)

    print('------------------------ After removing stop words ------------------------------')
    print()
    phraseList = remove_stopwords(text, stopwords_new)
    print(phraseList)
    print()

    print('------------------------ Score words ------------------------------')
    print()
    wordscores = calculate_word_scores(phraseList)
    print(wordscores)

    sortedKeywords = sorted(wordscores.items(), key=operator.itemgetter(1), reverse=True)

    print('------------------------ Sorted keywords ------------------------------')
    print()
    print(sortedKeywords)
    print((filter_sorted_keywords(sortedKeywords[:keyword_count])))

    if is_result_formatted:
        return jsonify(filter_sorted_keywords(sortedKeywords[:keyword_count]))
    else:
        return filter_keywords(sortedKeywords)

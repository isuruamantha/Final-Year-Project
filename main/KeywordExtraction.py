import re
import os
import operator
from time import strftime

import nltk
from flask import jsonify, make_response

debug = False
test = True
stopwords_new = []


# To check whether the number
def is_number(s):
    """
    :param s: Number input
    :return: Result
    """
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False


# To seperate the words
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


# To split the chapters
def split_chapter(full_text):
    """
    :param full_text: Full text
    :return: Splitted chapters
    """
    splited_words = []
    # splited_text = nltk.word_tokenize(full_text)
    splited_text = re.split('\n\n| \n|\n|[ ]|,', full_text)
    for word in splited_text:
        if not word == '':
            splited_words.append(word)
    return splited_words


# To remove the stop words
def remove_stopwords(split_sents, stop_word_list_new):
    """
    :param split_sents: Raw text
    :param stop_word_list_new: stop word list
    :return: text without stopwords
    """
    summed_phrase = []
    words = split_chapter(split_sents)
    for word in words:
        if word not in stop_word_list_new:
            summed_phrase.append(word)
    return summed_phrase


# Load the stopwords from the
def get_stopwords(stopwords):
    """
    :param stopwords: List of stop words
    :return: sorted stopwords list
    """
    stopwords_list = nltk.word_tokenize(stopwords)
    for word in stopwords_list:
        if not word.isdigit():
            stopwords_new.append(word)


# Calculate the score for words
def calculate_word_scores(phraseList):
    """
    :param phraseList: List of the phrases
    :return: calculated score
    """
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


# To generate score for each words
def generate_candidate_keyword_scores(phrase_list, word_score):
    """
    :param phrase_list: list of the phrases
    :param word_score: Score for each words
    :return: Generated score
    """
    keyword_candidates = {}
    for phrase in phrase_list:
        keyword_candidates.setdefault(phrase, 0)
        word_list = separate_words(phrase, 0)
        candidate_score = 0
        for word in word_list:
            candidate_score += word_score[word]
        keyword_candidates[phrase] = candidate_score
    return keyword_candidates


# To sort the words
def filter_sorted_keywords(sorted_keywords):
    """
    :param sorted_keywords: Input the sorted keywords
    :return: Filtered and formatted keywords
    """
    filterd_keyword_list = []
    for word in sorted_keywords:
        filterd_keyword_list.append(word[0])

    return keywords_json_formatter(filterd_keyword_list)


# To filter the words
def filter_keywords(sorted_keywords):
    """
    :param sorted_keywords: Raw sorted keywords
    :return: Filtered keywords list
    """
    filterd_keyword_list = []
    for word in sorted_keywords:
        filterd_keyword_list.append(word[0])

    return filterd_keyword_list


# To format the output
def keywords_json_formatter(unformatted_text):
    """
    :param unformatted_text:
    :return: Formatted text
    """
    topList = []

    for index, tex in enumerate(unformatted_text):
        tmpDict1 = {}
        tmpDict1["text"] = tex
        tmpDict1["size"] = 40 - index * 2
        topList.append(tmpDict1)

    return (topList)


# Stemming words
def stemming_words(tokens_list):
    """
    :param tokens_list:
    :return: Stemmed words
    """
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


# Main method
def keyword_extraction(sinhala_text, is_result_formatted, keyword_count, type):
    """
    :param sinhala_text: Input text
    :param is_result_formatted: Result should be formatted or not?
    :param keyword_count: count of the keywords
    :param type: category
    :return:
    """
    text = sinhala_text
    # text = "Sri Lanka's documented history spans 3,000 years, with evidence of pre-historic human settlements dating back to at least 125,000 years.[11] It has a rich cultural heritage and the first known Buddhist writings of Sri Lanka, the Pāli Canon, date back to the Fourth Buddhist council in 29 BC.[12][13] Its geographic location and deep harbours made it of great strategic importance from the time of the ancient Silk Road through to the modern Maritime Silk Road.[14][15][16] Sri Lanka was known from the beginning of British colonial rule as Ceylon (/sɪˈlɒn, seɪ-, siː-/). A nationalist political movement arose in the country in the early-20th century to obtain political independence, which was granted in 1948; the country became a republic and adopted its current name in 1972. Sri Lanka's recent history has been marred by a thirty-year civil war, which decisively ended when the Sri Lanka Armed Forces defeated the Liberation Tigers of Tamil Eelam (LTTE) in 2009.[17]"

    # Split text into sentences
    stopwords = open('assets/StopWords_sin.txt', 'r', encoding='utf-16').read()
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

    print('------------------------ Stemming the words ------------------------------')
    print()
    print(stemming_words(phraseList))

    print('------------------------ Score words ------------------------------')
    print()
    wordscores = calculate_word_scores(phraseList)
    print(wordscores)

    sortedKeywords = sorted(wordscores.items(), key=operator.itemgetter(1), reverse=True)

    print('------------------------ Sorted keywords ------------------------------')
    print()
    print(sortedKeywords)
    print((filter_sorted_keywords(sortedKeywords[:keyword_count])))

    if (type == "keyword"):
        if is_result_formatted:
            return jsonify(filter_sorted_keywords(sortedKeywords[:keyword_count]))
        else:
            return filter_keywords(sortedKeywords)
    else:
        if is_result_formatted:
            return jsonify(sortedKeywords[:keyword_count])
        else:
            return filter_keywords(sortedKeywords)

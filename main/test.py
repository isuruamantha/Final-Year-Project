import hashlib
import io
import json
import os
import pprint


# JSON test format for mind map

# json_list = {}
# json_list["class"] = "go.TreeModel"
# text = ["a", "b", "c", "e"]
# topList = []
# tmpDict1 = {}
# tmpDict1["key"] = 0
# tmpDict1["text"] = "Main Node"
# tmpDict1["loc"] = 0.0
#
# topList.append(tmpDict1)
#
# for index, tex in enumerate(text):
#     tmpDict1 = {}
#     tmpDict1["key"] = index + 1
#     tmpDict1["parent"] = 0
#     tmpDict1["text"] = tex
#     tmpDict1["brush"] = "skyblue"
#     tmpDict1["dir"] = "left"
#     topList.append(tmpDict1)
#
# json_list["nodeDataArray"] = (topList)
#
# pprint.pprint(json_list)


# JSON test format for keyword cloud

# json_list = {}
#
# text = ["a", "b", "c", "e"]
# topList = []
#
# for index, tex in enumerate(text):
#     tmpDict1 = {}
#     tmpDict1["key"] = index + 1
#     tmpDict1["value"] = 0
#     topList.append(tmpDict1)
#
# pprint.pprint(topList)
#
#
# def keywords_json_formatter():
#     topList = []
#
#     for index, tex in enumerate(text):
#         tmpDict1 = {}
#         tmpDict1["key"] = index + 1
#         tmpDict1["value"] = 0
#         topList.append(tmpDict1)
#
#     pprint.pprint(topList)
#
#
# import hashlib
# password = 'dulika'
# h = hashlib.md5(password.encode())
# print(len(h.hexdigest()))
# print(h.hexdigest())


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


print(stemming_words(["අංකද", "අටලක්ෂයකට", "අනාගත", "තුළ", "ආරම්‌භ"]))

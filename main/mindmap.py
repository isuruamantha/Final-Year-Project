import pprint

from flask import json, jsonify, app
from nltk import sent_tokenize

from summarization import textRankAlgorithm, sentence_splitter


def generate_mindmap_json(sorted_text):
    json_list = {}

    json_list["class"] = "go.TreeModel"

    text = sorted_text

    topList = []
    tmpDict1 = {}
    tmpDict1["key"] = 0
    tmpDict1["text"] = "Main Nodes"
    tmpDict1["loc"] = 0.0

    topList.append(tmpDict1)

    for index, tex in enumerate(text):
        tmpDict1 = {}
        tmpDict1["key"] = index + 1
        tmpDict1["parent"] = 0
        tmpDict1["text"] = tex
        tmpDict1["brush"] = "skyblue"
        tmpDict1["dir"] = "left"
        topList.append(tmpDict1)

    json_list["nodeDataArray"] = (topList)

    # pprint.pprint(json_list)
    return jsonify(json_list)


# return jsonify({"class": "go.TreeModel",
#                 "nodeDataArray": [
#                     {"key": 0, "text": "තොරතුරු තාක්‍ෂණය", "loc": "0 0"},
#                     {"key": 1, "parent": 0,
#                      "text": "අ.පො.ස. සාමාන්‍ය පෙළ සහ උසස්‌ පෙළ සඳහා අතිරේක විෂයක්‌ ලෙස තොරතුරු තාක්‍ෂණය(ICT සහ GIT) හඳුන්‌වා දීම මෙහි ලා අගය කළ යුතු ක්‍රියාමාර්‌ගයකි",
#                      "brush": "skyblue", "dir": "right",
#                      "loc": "77 -22"},
#                     {"key": 11, "parent": 1, "text": "Wake up early", "brush": "skyblue", "dir": "right",
#                      "loc": "200 -48"},
#                     {"key": 10,"parent": 1, "text": "Delegate", "brush": "skyblue", "dir": "right",
#                      "loc": "200 -22"},
#                     {"key": 13, "parent": 1, "text": "Simplify", "brush": "skyblue", "dir": "right",
#                      "loc": "200 4"},
#                     {"key": 2, "parent": 0,
#                      "text": "පහුගිය කාලය තුළ Mozilla Firefox, ලිනක්‌ස්‌ මෙහෙයුම්‌ පද්‌ධති වගේම Microsoft Windows Vista සහ MS Office 2007 පැකේජයන්‌ පවා සිංහලට පැමිණීම මෙහිලා විශේෂ කොට දක්‌වන්‌න පුලුවන්",
#                      "brush": "darkseagreen",
#                      "dir": "right", "loc": "77 43"},
#                     {"key": 21, "parent": 2, "text": "Planning", "brush": "darkseagreen", "dir": "right",
#                      "loc": "203 30"},
#                     {"key": 211, "parent": 21, "text": "Priorities", "brush": "darkseagreen", "dir": "right",
#                      "loc": "274 17"},
#                     {"key": 212, "parent": 21, "text": "Ways to focus", "brush": "darkseagreen", "dir": "right",
#                      "loc": "274 43"},
#                     {"key": 22, "parent": 2, "text": "Goals", "brush": "darkseagreen", "dir": "right",
#                      "loc": "203 56"},
#                     {"key": 3, "parent": 0,
#                      "text": "පළමුව දේශීය ඵලදායිතාව නැංවීම සඳහා අවශ්‍ය තොරතුරු තාක්‍ෂණය දැනුම ඉහල දැමිය යුතුය.",
#                      "brush": "palevioletred", "dir": "left",
#                      "loc": "-20 -31.75"},
#                     {"key": 31, "parent": 3, "text": "Too many meetings", "brush": "palevioletred",
#                      "dir": "left", "loc": "-117 -64.25"},
#                     {"key": 32, "parent": 3, "text": "Too much time spent on details", "brush": "palevioletred",
#                      "dir": "left", "loc": "-117 -25.25"},
#                     {"key": 33, "parent": 3, "text": "Message fatigue", "brush": "palevioletred", "dir": "left",
#                      "loc": "-117 0.75"},
#                     {"key": 331, "parent": 31, "text": "Check messages less", "brush": "palevioletred",
#                      "dir": "left", "loc": "-251 -77.25"},
#                     {"key": 332, "parent": 31, "text": "Message filters", "brush": "palevioletred",
#                      "dir": "left", "loc": "-251 -51.25"},
#                     {"key": 4, "parent": 0, "text": "Isuru Amantha", "brush": "coral", "dir": "left",
#                      "loc": "-20 52.75"},
#                     {"key": 41, "parent": 4, "text": "Methods", "brush": "coral", "dir": "left",
#                      "loc": "-103 26.75"},
#                     {"key": 42, "parent": 4, "text": "Deadlines", "brush": "coral", "dir": "left",
#                      "loc": "-103 52.75"},
#                     {"key": 43, "parent": 4, "text": "Checkpoints", "brush": "coral", "dir": "left",
#                      "loc": "-103 78.75"}
#                 ]
#                 })


def mindmap_generate(sinhala_text):
    generated_sinahala_summary = textRankAlgorithm(sinhala_text);
    sents_list = sent_tokenize(generated_sinahala_summary)

    print(sents_list[:4])

    print("Keywords list")

    # all_extracted_keywords = keyword_extraction(sinhala_text)
    # print(all_extracted_keywords)

    return generate_mindmap_json(sents_list[:4])


'''
Get all the extracted keywords
send the the one sentence
loop and findout the keywords
'''

# mindmap_generate(
#     "තොරතුරු තාක්‍ෂණය දේශීයකරණය දැන්‌ සැම තැනම කතා කරන මාතෘකාවක්‌ වෙලා. පහුගිය කාලය තුළ Mozilla Firefox, ලිනක්‌ස්‌ මෙහෙයුම්‌ පද්‌ධති වගේම Microsoft Windows Vista සහ MS Office 2007 පැකේජයන්‌ පවා සිංහලට පැමිණීම මෙහිලා විශේෂ කොට දක්‌වන්‌න පුලුවන්‌. එමෙන්‌ම නුදුරු අනාගතයේදී තව තවත්‌ වටිනා මෘදුකාංග දේශීයකරණය වෙනු ඇති. ඉංග්‍රීසි මෘදුකාංග වලට සිංහල අතුරු මුහුණත්‌ (interface) සැකසීම දේශීයකරණයට ප්‍රමාණවත්‌ නොවේ, පරිශීලකයා අනුව ක්‍රියාකාරකම් හා පෙර ලැබූ පළපුරුද්ද එකතු කලයුතුය(පරිශීලන අත්දැකීම). අපගේ දැක්‌ම අනුව දේශීයකරණය දෙයාකාරයකින්‌ සිදුවිය යුතු යි. පළමුව දේශීය ඵලදායිතාව නැංවීම සඳහා අවශ්‍ය තොරතුරු තාක්‍ෂණය දැනුම ඉහල දැමිය යුතුය. ගොවිපලේ සිට කර්‌මාන්‌ත සහ කාර්‌යාලීය මට්‌ටම දක්‌වා තොරතුරු තාක්‍ෂණය භාවිතා කිරීමට ඇති හැකියාව වැඩි දියුණු කිරීම මේ යටතට වැටේ. භාෂාව මේ සඳහා විශාල බාධකයක්‌ විය හැකි බැවින්‌ දේශීයකරණයට සිදු කිරීමේදී ඒ ඒ අංශයන්‌ගෙන්‌ රටට සිදුව ඍජු සහ වක්‍ර බලපෑම්‌ අනුව ඒවාට ප්‍රමුඛතාවය ලබා දී ක්‍රියාත්‌මක කළ යුතුය. දෙවන කොටසට අයිති වනුයේ තොරතුරු තාක්‍ෂණය භාවිතා කිරීම සඳහා තාක්‍ෂණවේදීන්‌ සැකසීමේ කාර්‌යයයි. මේ සඳහා ක්‍රමවත්‌ අධ්‍යාපන ක්‍රමයක්‌ සැකසීම සහ ඒ සඳහා අවශ්‍ය පහසුකම්‌ ශිෂ්‍ය ශිෂ්‍යාවන්‌ට සහ දැනට එම ක්‍ෂේත්‍රෙය්‌ නියැලෙන අයට ලබාදීම අනිවාර්‌ය වේ. අ.පො.ස. සාමාන්‍ය පෙළ සහ උසස්‌ පෙළ සඳහා අතිරේක විෂයක්‌ ලෙස තොරතුරු තාක්‍ෂණය(ICT සහ GIT) හඳුන්‌වා දීම මෙහි ලා අගය කළ යුතු ක්‍රියාමාර්‌ගයකි. එසේම නව විෂය නිර්‌දේශය යටතේ උසස්‌ පෙළ ප්‍රධාන විෂයක්‌ ලෙස තොරතුරු තාක්‍ෂණය (IT) ඉගැන්‌වීමට ආරම්‌භ කිරීම වඩාත්‌ අගය කළ යුතුය. ඉතා වටිනා අගය කළයුතු විෂය නිර්‌දේශයකින්‌ එය සමන්‌විතය. අපගේ දැක්‌මට අනුව දැනට අරටුව ශක්‌තිමත්‌ව සැකසෙමින්‌ පවතී. අනෙකුත්‌ බාහිර කරුණු ද, එයට අවශ්‍ය කරන ශක්‌තිය ද ලබාදේ නම්‌ ත්‍රස්‌තවාදයෙන්‌ මිදුනු අපේ රටට අහිමිව ගිය ආර්‌ථික ස්‌ථානයද නැවත හිමිකරදීමට අනාගත පරපුරට හැකි වනු නොඅනුමානය.")

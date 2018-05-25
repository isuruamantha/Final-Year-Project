import pprint
import random

from flask import json, jsonify, app
from nltk import sent_tokenize, re

from KeywordExtraction import keyword_extraction
from summarization import textrank_algorithm, sentence_splitter


# Create mind map according to the layout
def generate_mindmap_json(sorted_text, keyword_list):
    json_list = {}

    json_list["class"] = "go.TreeModel"

    text = sorted_text

    directions = ['right', 'left']
    colors = ['skyblue', 'red', 'green', 'MAROON', 'YELLOW', 'TEAL', 'BLUE', 'PURPLE']

    topList = []
    tmpDict1 = {}
    tmpDict1["key"] = 0
    tmpDict1["text"] = "Mind Map"
    tmpDict1["loc"] = 0.0

    topList.append(tmpDict1)

    for index, tex in enumerate(text):

        tmpDict2 = {}
        random_selected_color = random.choice(colors)
        random_selected_direction = random.choice(directions)
        tmpDict2["key"] = index + 1
        tmpDict2["parent"] = 0
        tmpDict2["text"] = tex
        tmpDict2["brush"] = random_selected_color
        tmpDict2["dir"] = random_selected_direction
        topList.append(tmpDict2)
        for loop_idx, tokenized_word in enumerate(word_tokenize(tex)):
            tmpDict3 = {}
            # if set(keyword_list).intersection(tokenized_word):
            if any(word in tokenized_word for word in keyword_list):
                tmpDict3["key"] = loop_idx + 100 + 1
                tmpDict3["parent"] = index + 1
                tmpDict3["text"] = tokenized_word
                tmpDict3["brush"] = random_selected_color
                tmpDict3["dir"] = random_selected_direction
                topList.append(tmpDict3)

    json_list["nodeDataArray"] = (topList)

    return jsonify(json_list)


# To filterd out the sorted keywords
def filter_sorted_keywords(sorted_keywords):
    filterd_keyword_list = []
    for word in sorted_keywords:
        filterd_keyword_list.append(word[0])

    return filterd_keyword_list


# To tokenize thw words
def word_tokenize(full_text):
    splited_words = []
    # splited_text = nltk.word_tokenize(full_text)
    splited_text = re.split('\n\n| \n|\n|[ ]|,', full_text)
    for word in splited_text:
        if not word == '':
            splited_words.append(word)
    return splited_words


# Main method
def mindmap_generate(sinhala_text, sentence_count, keyword_count):
    generated_sinahala_summary = textrank_algorithm(sinhala_text, sentence_count);
    sents_list = sent_tokenize(generated_sinahala_summary)

    print(sents_list[:4])

    all_extracted_keywords = keyword_extraction(sinhala_text, False, keyword_count, "keyword")

    print('------------------------ Extracted Keywords list ------------------------------')
    print()
    print(all_extracted_keywords)

    return generate_mindmap_json(sents_list[:sentence_count], all_extracted_keywords[:keyword_count])

# For test purpose
# mindmap_generate(
#     "තොරතුරු තාක්‍ෂණය දේශීයකරණය දැන්‌ සැම තැනම කතා කරන මාතෘකාවක්‌ වෙලා. පහුගිය කාලය තුළ Mozilla Firefox, ලිනක්‌ස්‌ මෙහෙයුම්‌ පද්‌ධති වගේම Microsoft Windows Vista සහ MS Office 2007 පැකේජයන්‌ පවා සිංහලට පැමිණීම මෙහිලා විශේෂ කොට දක්‌වන්‌න පුලුවන්‌. එමෙන්‌ම නුදුරු අනාගතයේදී තව තවත්‌ වටිනා මෘදුකාංග දේශීයකරණය වෙනු ඇති. ඉංග්‍රීසි මෘදුකාංග වලට සිංහල අතුරු මුහුණත්‌ (interface) සැකසීම දේශීයකරණයට ප්‍රමාණවත්‌ නොවේ, පරිශීලකයා අනුව ක්‍රියාකාරකම් හා පෙර ලැබූ පළපුරුද්ද එකතු කලයුතුය(පරිශීලන අත්දැකීම). අපගේ දැක්‌ම අනුව දේශීයකරණය දෙයාකාරයකින්‌ සිදුවිය යුතු යි. පළමුව දේශීය ඵලදායිතාව නැංවීම සඳහා අවශ්‍ය තොරතුරු තාක්‍ෂණය දැනුම ඉහල දැමිය යුතුය. ගොවිපලේ සිට කර්‌මාන්‌ත සහ කාර්‌යාලීය මට්‌ටම දක්‌වා තොරතුරු තාක්‍ෂණය භාවිතා කිරීමට ඇති හැකියාව වැඩි දියුණු කිරීම මේ යටතට වැටේ. භාෂාව මේ සඳහා විශාල බාධකයක්‌ විය හැකි බැවින්‌ දේශීයකරණයට සිදු කිරීමේදී ඒ ඒ අංශයන්‌ගෙන්‌ රටට සිදුව ඍජු සහ වක්‍ර බලපෑම්‌ අනුව ඒවාට ප්‍රමුඛතාවය ලබා දී ක්‍රියාත්‌මක කළ යුතුය. දෙවන කොටසට අයිති වනුයේ තොරතුරු තාක්‍ෂණය භාවිතා කිරීම සඳහා තාක්‍ෂණවේදීන්‌ සැකසීමේ කාර්‌යයයි. මේ සඳහා ක්‍රමවත්‌ අධ්‍යාපන ක්‍රමයක්‌ සැකසීම සහ ඒ සඳහා අවශ්‍ය පහසුකම්‌ ශිෂ්‍ය ශිෂ්‍යාවන්‌ට සහ දැනට එම ක්‍ෂේත්‍රෙය්‌ නියැලෙන අයට ලබාදීම අනිවාර්‌ය වේ. අ.පො.ස. සාමාන්‍ය පෙළ සහ උසස්‌ පෙළ සඳහා අතිරේක විෂයක්‌ ලෙස තොරතුරු තාක්‍ෂණය(ICT සහ GIT) හඳුන්‌වා දීම මෙහි ලා අගය කළ යුතු ක්‍රියාමාර්‌ගයකි. එසේම නව විෂය නිර්‌දේශය යටතේ උසස්‌ පෙළ ප්‍රධාන විෂයක්‌ ලෙස තොරතුරු තාක්‍ෂණය (IT) ඉගැන්‌වීමට ආරම්‌භ කිරීම වඩාත්‌ අගය කළ යුතුය. ඉතා වටිනා අගය කළයුතු විෂය නිර්‌දේශයකින්‌ එය සමන්‌විතය. අපගේ දැක්‌මට අනුව දැනට අරටුව ශක්‌තිමත්‌ව සැකසෙමින්‌ පවතී. අනෙකුත්‌ බාහිර කරුණු ද, එයට අවශ්‍ය කරන ශක්‌තිය ද ලබාදේ නම්‌ ත්‍රස්‌තවාදයෙන්‌ මිදුනු අපේ රටට අහිමිව ගිය ආර්‌ථික ස්‌ථානයද නැවත හිමිකරදීමට අනාගත පරපුරට හැකි වනු නොඅනුමානය.")

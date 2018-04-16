import codecs
import unicodedata

import nltk
from nltk.tag import StanfordNERTagger
from nltk.metrics.scores import accuracy

# raw_annotations = codecs.open('train.txt', encoding='utf-8')
# raw_annotations = open("train.txt", encoding="utf-8", errors='ignore').read()

raw_annotations = """"
හයිටිය	B-NE 
තමා	O 
හයිටිය	B-NE 
අතහැර	O 
පලා	O 
ගියේ	O 
කැමැත්තකින්	O 
නොව	O 
ඇමරිකාවේ	B-NE 
බල	O 
කිරීම	O 
නිසා	O 
"""

split_annotations = raw_annotations.split()
print(split_annotations)

# Amend class annotations to reflect Stanford's NERTagger
for n, i in enumerate(split_annotations):
    if i == "B-NE":
        split_annotations[n] = "BEG NE"
    if i == "I-NE":
        split_annotations[n] = "MID NE"
    if i == "O":
        split_annotations[n] = "OTHER"

print(split_annotations[0])


# Group NE data into tuples
def group(lst, n):
    for i in range(0, len(lst), n):
        val = lst[i:i + n]
        if len(val) == n:
            yield tuple(val)


reference_annotations = list(group(split_annotations, 2))
pure_tokens = split_annotations[::2]
print(pure_tokens)

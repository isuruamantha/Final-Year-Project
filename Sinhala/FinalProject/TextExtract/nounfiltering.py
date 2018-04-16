from googletrans import Translator
import nltk, re
from nltk import sent_tokenize, word_tokenize, pos_tag


#contents = open('testfile.txt','r', encoding='utf-8').read()
contents = open('tagged1.TXT','r', encoding='utf-16').read()
tagged_words = re.split('; |, |\*|\n|[ ]', contents)
print(tagged_words)
#sentences = nltk.sent_tokenize(contents)

file1 = open('tagged_file.txt', 'w')
nnpi_list = []
nnn_list = []
nnpa_list = []
sent_item = []
translator = Translator()


def noun_filter(sent_item):
    if sent_item[0] and not sent_item[0] == '.':
        if sent_item[1] == 'NNPI':
            if sent_item[0] not in nnpi_list:
                nnpi_list.append(sent_item[0])
        elif sent_item[1] == 'NNPA':
            if sent_item[0] not in nnpa_list:
                nnpa_list.append(sent_item[0])
        elif sent_item[1] == 'NNN':
            if sent_item[0] not in nnn_list:
                nnn_list.append(sent_item[0])


for tagged_word in tagged_words:
    sent_item = tagged_word.split('_')
    '''print(sent_item)
        for item in sent_item:
            print(item)'''
    noun_filter(sent_item)

'''for sent in sentences:
    tagged_sent = nltk.pos_tag(word_tokenize(sent)) #sinhala POS tagging should be here
    #print(tagged_sent)
    for sent_item in tagged_sent:
        noun_filter(sent_item)
        if sent_item[0] == '.' or sent_item[0] == '*' or sent_item[0] == ')':
            item = '\n'
        elif sent_item[0] == ',' or sent_item[0] == "'" or sent_item[0] == '(' or sent_item[0] == ')':
            item = ""
        elif sent_item[0].isdigit():
            item = ''
        else:
            item = sent_item[0] + "_" + sent_item[1] + " "
        with open('tagged_file.txt', 'a', encoding='utf-8') as the_file:
            the_file.writelines(item)
    file1.close()'''

#list NNP and NN words
print('NNPI list ->')
print(nnpi_list)
print('NNPA list ->')
print(nnpa_list)
print('NNN list ->')
print(nnn_list)


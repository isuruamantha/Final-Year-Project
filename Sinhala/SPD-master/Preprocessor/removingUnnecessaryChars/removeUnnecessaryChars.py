import re
import string


class removeUnnecessaryChars:
    def remove_chars(self, text):
        cyril = re.compile(u'[\u0021-\u007F]', re.UNICODE)

        plaiText = cyril.sub('', str(text))

        return plaiText

    def replaceNumbers(self, text):
        # Iterate through the string, replacing "0" for the digits
        for i in text:
            if i.isdigit():
                text = text.replace(i, "0")
        return text

    def removePunctuation(self, text):
        # remove all the punctuation marks
        for c in string.punctuation:
            text = text.replace(c, "")
        return text

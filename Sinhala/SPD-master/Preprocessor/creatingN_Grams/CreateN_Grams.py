from nltk import ngrams


class CreateN_Grams:

    @staticmethod
    def createN_Grams(list, ngramValue):
        ngramArray = []
        n = ngramValue

        trigrams = ngrams(list, n)
        for grams in trigrams:
            ngramArray.append(grams)

        return ngramArray

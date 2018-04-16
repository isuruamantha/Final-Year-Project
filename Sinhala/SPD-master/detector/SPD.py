from sklearn.feature_extraction.text import TfidfVectorizer

from Preprocessor.QuoteRemover import QuoteRemover
from Preprocessor.creatingN_Grams.CreateN_Grams import CreateN_Grams
from Preprocessor.removingStopWords.RemovingStopWords import RemovingStopWords
from Preprocessor.removingUnnecessaryChars.removeUnnecessaryChars import removeUnnecessaryChars
from Preprocessor.replacingSynonyms.SynonymReplacer import SynonymReplacer
from Preprocessor.stemming.StemmingSinhala import StemmingSinhala
from Preprocessor.tokenizing.TokenizeText import TokenizeText


class SPD:
    @staticmethod
    def standardize(doc):
        print("Input: %r" % doc)

        text = QuoteRemover.remove_quotes(doc)
        print("Removed quotes: %r" % text)

        remove_unnecessary = removeUnnecessaryChars()
        text = remove_unnecessary.removePunctuation(text)
        print("Removed punctuations: %r" % text)

        text = remove_unnecessary.replaceNumbers(text)
        print("Numbers replaced: %r" % text)

        tokenizer = TokenizeText()
        tokens_list = tokenizer.tokenizeText(text)
        print("Tokens: %r" % tokens_list)

        stop_words_remover = RemovingStopWords()
        output = stop_words_remover.removeStopwords(tokens_list)
        tokens_list = output
        print("Removed stop words: %r" % output)

        stemming = StemmingSinhala()
        tokens_list = stemming.stem(tokens_list)
        print("Stemmed: %r" % tokens_list)

        replaced_synonyms = SynonymReplacer()
        synonyms_replaced_list = replaced_synonyms.replace_synonyms(tokens_list)
        tokens_list = synonyms_replaced_list
        print("Synonym replaced: %r" % synonyms_replaced_list)

        n_gram_list = CreateN_Grams.createN_Grams(tokens_list, 3)
        print("N-grams: %r" % n_gram_list)

        standardized_text = " ".join(tokens_list)
        print("Standardized Text: %r" % standardized_text)
        return standardized_text

    @staticmethod
    def compare(docs):
        documents = [x['standardized_content'] for x in docs]
        tf_idf = TfidfVectorizer().fit_transform(documents)
        # no need to normalize, since Vectorizer will return normalized tf-idf
        pairwise_similarity = tf_idf * tf_idf.T
        # All I want is the last row
        similarities = pairwise_similarity.toarray().tolist()[-1][:-1]

        uniquenesses = [1 - x for x in similarities]
        results = {
            'similarities': [],
            'uniqueness': round(min(uniquenesses) * 100, 2) if len(uniquenesses) > 0 else 100
        }

        for i, x in enumerate(similarities):
            results['similarities'].append({
                'name': docs[i]['name'],
                'similarity': round(x * 100, 2)
            })
        return results

    @staticmethod
    def compare_uploaded_files(docs):
        texts = [x['text'] for x in docs]
        tf_idf = TfidfVectorizer().fit_transform(texts)
        # no need to normalize, since Vectorizer will return normalized tf-idf
        pairwise_similarity = tf_idf * tf_idf.T
        similarities = pairwise_similarity.toarray().tolist()

        uniqueness = SPD.find_uniqueness(similarities)
        uniqueness = [
            {
                'file': docs[i]['name'],
                'uniqueness': round(x * 100, 2)
            } for i, x in enumerate(uniqueness)
        ]
        print(uniqueness)

        docs = [
            {
                'file': docs[i]['name'],
                'similarities': [
                    {
                        'file': docs[j]['name'],
                        'similarity': round(y * 100, 2)
                    } for j, y in enumerate(x)
                ]
            } for i, x in enumerate(similarities)
        ]

        docs = SPD.find_closest_files(docs)
        print(docs)

        return uniqueness, docs

    @staticmethod
    def find_uniqueness(similarity_list):
        result_list = []

        for index in range(0, len(similarity_list)):
            similarities = [x for i, x in enumerate(similarity_list[index]) if i != index]
            uniqueness = 1 - (max(similarities) if len(similarities) > 0 else 0)

            print(uniqueness)
            result_list.append(uniqueness)

        return result_list

    @staticmethod
    def find_closest_files(docs):
        for doc in docs:
            doc['similarities'] = sorted(doc['similarities'], key=lambda k: k['similarity'], reverse=True)
            doc['similarities'] = [x for x in doc['similarities'] if x['file'] != doc['file']][0:1]
        return docs

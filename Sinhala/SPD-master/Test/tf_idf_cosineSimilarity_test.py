from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

train_set = ("The sky is blue.", "The sun is bright.")
test_set = ("The sun in the sky is bright.",
            "We can see the shining sun, the bright sun.")

print(train_set)
stopWords = stopwords.words('english')
vectorizer = CountVectorizer(stop_words=stopWords)
print(vectorizer.fit_transform(train_set))

print(vectorizer.vocabulary)
smatrix = vectorizer.transform(test_set)
print(smatrix)
print(smatrix.todense())
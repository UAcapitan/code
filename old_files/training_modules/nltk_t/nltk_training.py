import nltk
nltk.download('punkt')

text = 'Hello, my dear friend. What`s new Mr.Anderson did? How are you?'

t = nltk.tokenize.sent_tokenize(text)
print(t)

w = nltk.tokenize.word_tokenize(text)
print(w)

p = nltk.probability.FreqDist(w)
print(p)
print(p.most_common(3))
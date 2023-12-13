
import re


# Generator realization
class SentenceGen:
    def __init__(self, text):
        self._text = text
        self._words = re.compile("\w+").findall(text)

    def __repr__(self):
        return self._text

    def __iter__(self):
        for word in self._words:
            yield word
        return


# Iterator lazy realization
class SentenceIter:
    def __init__(self, text):
        self._text = text

    def __repr__(self):
        return self._text

    def __iter__(self):
        return (match.group() for match in re.compile("\w+").finditer(self._text))


if __name__ == "__main__":

    # Generator
    sentence_gen = SentenceGen("One two three")
    print(sentence_gen)

    for word in sentence_gen:
        print(word)


    # Lazy iterator
    sentence_iter = SentenceIter("One two three")
    print(sentence_gen)

    for word in sentence_gen:
        print(word)


import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_word_definition(word):
    try:
        url = f"https://www.dictionary.com/browse/{word}"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        definition_element = soup.find("div", {"data-type": "word-definition-content"}).find("p")

        if definition_element:
            definition = definition_element.get_text()
        else:
            definition = ""

        return definition
    except:
        return ""

def get_translated_word(word):
    try:
        translator = Translator()
        translation = translator.translate(word, src='en', dest='uk')
        return translation.text
    except:
        return ""

print(get_word_definition("python"))
print(get_translated_word("python"))

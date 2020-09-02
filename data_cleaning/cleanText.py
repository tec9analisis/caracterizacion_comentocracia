import requests
from bs4 import BeautifulSoup
import unidecode
from nltk.corpus import stopwords
import re
from collections import Counter
import pandas as pd

path = r'C:\Users\Lenovo\Documents\Words.csv'
url = 'https://www.bbc.com/mundo/noticias-53435056'
def scraping(url):
    article = requests.get(url)
    article.encoding = 'utf8'
    soupA = BeautifulSoup(article.text, 'html.parser')
    return soupA.find_all('p')

extractText = scraping(url)
extractText = extractText[12:92]

def cleanTokens(extractText):
    text = [' '.join(extractText[i].text.strip().split()) for i in range(len(extractText))]
    words = [re.findall(r'\w+', text[i].lower(), flags = re.UNICODE) for i in range(len(text))]
    print(words)
    return [word for i in range(len(words)) for word in words[i] if word not in stopwords.words('spanish')]
words = cleanTokens(extractText)

df = pd.DataFrame.from_dict(Counter(words), orient='index').reset_index()
df.to_csv(path, index = False)

#lematizar
import spacy
nlp = spacy.load('es_core_news_md')

nlpText = [nlp(extractText[i].text) for i in range(len(extractText))]
lemmas = [tok.lemma_.lower() for i in range(len(nlpText)) for tok in nlpText[i]]
lemmas

bagWords = [word for word in lemmas if word not in stopwords.words('spanish')]
[re.findall(r'\w+', bagWords.lower(), flags = re.UNICODE) for i in range(len(bagWords))]

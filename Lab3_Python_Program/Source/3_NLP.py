import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

import re
import urllib.request

def tokens(text):
    """
    Get all words from the corpus
    """
    return re.findall('[a-z]+', text.lower())

#Reading Text file
with open("inputTextfile",'r') as f:
    content = f.read()

WORDS = tokens(open('inputTextfile').read())
print(WORDS)
print(content)

#Tokenization
from nltk.stem import WordNetLemmatizer
print("\n")
print("LEMMATIZATION")
lemmatize_list = []
lemmatizer=WordNetLemmatizer()
for WORD in WORDS:
    print(lemmatizer.lemmatize(WORD))

#Bi-GRAM
from nltk import word_tokenize
from nltk.util import ngrams
print("\n\n")
print("BI-GRAM")
input_list = []
for WORD in WORDS:
    input_list=input_list+[WORD]

def find_trigrams(input_list):
  bigram_list = []
  for i in range(len(input_list)-2):
      bigram_list.append((input_list[i], input_list[i+1]))
  return bigram_list
print(find_trigrams(input_list))
print("\n")

#Bi-gram frequency
print("\n")
print("BIGRAM FREQUENCY")
frequencies = Counter([])
bigrams = ngrams(WORDS, 2)
frequencies += Counter(bigrams)
print(frequencies)

#Top five bi-gram word
print("\n")
print("TOP FIVE BI-GRAM WORDS")
topFiveBG=list()
for i in range (0,5) :
    topFiveBG.append(" ".join(re.findall("[a-zA-Z]+",str(frequencies).split(":")[i])))
print(topFiveBG)

#Finding all the sentences with those most repeated bi-grams
print("\n")
print("ALL SENTENCE WITH MOST BI-GRAM WORDS")
lines={}
for line in content.split("."):
    for word in topFiveBG:
        if word in line:
            if line in lines:
                pass
            else:
                lines[line]=""
result=list()
for line in lines:
    result.append(line+".")
print(result)
from collections import defaultdict
from typing import DefaultDict
import pandas
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('wordnet')

docs = {
	1: 'new home sales top forecasts new',
	2: 'home sales rise in july',
	3: 'increase in home sales in july',
	4: 'july new home sales rise'	
}

def tokenizer(text):
	return text.split()

def normalizer(arr):
	lemmatizer=WordNetLemmatizer()
	new_arr = []
	for word in arr:
		new_arr.append(lemmatizer.lemmatize(word))

	return new_arr

def indexer(dic):
	index = defaultdict(list)

	for id in sorted(dic.keys()):
		term_set = set(normalizer(tokenizer(dic[id]))) #set to avoid duplicates
		print(term_set)
		for term in term_set:
			index[term].append(id)

	return index





index = indexer(docs)

print(index['july'])

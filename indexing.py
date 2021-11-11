from typing import DefaultDict
import pandas
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('wordnet')



doc1 = 'new home sales top forecasts new'
doc2 = 'home sales rise in july'
doc3 = 'increase in home sales in july'
doc4 = 'july new home sales rise'

def tokenizer(text):
	return text.split()

def normalizer(arr):
	lemmatizer=WordNetLemmatizer()
	new_arr = []
	for word in arr:
		new_arr.append(lemmatizer.lemmatize(word))

	return new_arr

def classifier(arr, docID):
	bag = []
	for term in arr:
		bag.append((term, docID))

	return bag
	
def indexer(arr):
	term_ID_list = []

	for i, doc in enumerate(arr):
		doc_term_list = classifier(normalizer(tokenizer(doc)), i+1)
		for term in doc_term_list:
			term_ID_list.append(term)

	dic = {}
	
	for term, docID in term_ID_list:
		if term in dic: 
			print(term, 'exists already', dic[term])
			dic[term].append(docID)
		else:
			dic[term] = [docID]

	return dic




doc_arr = [doc1, doc2, doc3, doc4]
index = indexer(doc_arr)

print(index['new'])

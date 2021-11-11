import pandas
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('wordnet')



doc1 = 'new home sales top forecasts'
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

print(normalizer(tokenizer(doc1)))
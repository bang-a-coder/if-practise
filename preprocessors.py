import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('wordnet')

def tokenizer(text):
	return text.split()

def normalizer(arr):
	lemmatizer=WordNetLemmatizer()
	new_arr = []
	for word in arr:
		new_arr.append(lemmatizer.lemmatize(word.lower()))

	return new_arr
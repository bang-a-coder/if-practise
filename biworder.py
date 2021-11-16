from preprocessors import normalizer, tokenizer
from preprocessors import normalizer, tokenizer

#create possible biwords of a given string
def biworder(text):
	terms = normalizer(tokenizer(text))
	res = []

	i = 0
	while i < len(terms) -1:
		res.append(terms[i] + ' ' + terms[i+1])
		i += 1

	return res
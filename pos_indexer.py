from collections import defaultdict
from preprocessors import normalizer,tokenizer

docs = {
	1: 'new home sales top forecasts new',
	2: 'home sales rise in july',
	3: 'increase in home sales in july',
	4: 'july new home sales rise',
	5: 'breakthrough drug for schizophrenia',
	6: 'new schizophrenia drug',
	7: 'new approach for treatment of schizophrenia new hopes for schizophrenia patients',
	8: 'The inventor Stanford Ovshinsky never went to university',
	9: 'Jonathan went to Stanford University last year'
}

def pos_indexer(dic):
	split_dic = {}

	for key, text in dic.items():
		split_dic[key] = normalizer(tokenizer(text))

	pos_index = defaultdict(set)

	for key, tokens in split_dic.items():
		for token in tokens:
			pos_index[token] = defaultdict(set)

			for key, tokens in split_dic.items():
				return


	return split_dic

print(pos_indexer(docs))
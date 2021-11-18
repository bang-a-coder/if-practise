from collections import defaultdict
from preprocessors import normalizer,tokenizer

docs = {
	1: 'new home sales top forecasts new',
	2: 'home sales rise in july',
	3: 'increase in home sales in july',
	4: 'july new home sales rise new',
	5: 'breakthrough drug for schizophrenia new',
	6: 'new schizophrenia drug new',
	7: 'new approach for new treatment of schizophrenia new hopes for schizophrenia patients',
	8: 'The inventor Stanford Ovshinsky never went to university',
	9: 'Jonathan went to Stanford University last year'
}

def pos_indexer(dic):
	split_dic = defaultdict(set)

	for key, text in dic.items():
		split_dic[key] = normalizer(tokenizer(text))


	pos_index = defaultdict(set)

	for key, tokens in split_dic.items():
		for token in tokens:
			pos_index[token] = defaultdict(set)

			for key2, takens in split_dic.items():
				pos_index[token][key2] = [index for index in range(
    									len(takens)) if takens[index] == token]


	return pos_index

print(pos_indexer(docs)['new'])
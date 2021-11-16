from collections import defaultdict
import preprocessors
from preprocessors import normalizer,tokenizer

docs = {
	1: 'new home sales top forecasts new',
	2: 'home sales rise in july',
	3: 'increase in home sales in july',
	4: 'july new home sales rise',
	5: 'breakthrough drug for schizophrenia',
	6: 'new schizophrenia drug',
	7: 'new approach for treatment of schizophrenia new hopes for schizophrenia patients'
}



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

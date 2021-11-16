from collections import defaultdict
import preprocessors
from preprocessors import normalizer,tokenizer
import queers
from queers import and_query, or_query
from biworder import biworder

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



def indexer(dic, method = 'def'):
	index = defaultdict(list)

	for id in sorted(dic.keys()):
		if method == 'bi':
			term_set = set(biworder(dic[id]))
		else:
			term_set = set(normalizer(tokenizer(dic[id]))) #set to avoid duplicates

		# print(term_set)
		for term in term_set:
			index[term].append(id)

	return index





index = indexer(docs)

# print(index['stanford university'])
print(and_query('Stanford University', index))

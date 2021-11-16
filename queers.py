import preprocessors
from preprocessors import normalizer, tokenizer

def and_merge(sorted_list1, sorted_list2):
    merged_list = []
    # first we make copies of the lists, so we don't modify the existing lists in the index:
    list1 = list(sorted_list1)
    list2 = list(sorted_list2)

    #iterators
    it_1 = 0
    it_2 = 0

    while it_1 < len(list1) and it_2 < len(list2): #  checking if it exceeds the max len of any list, merge_list can have at most len(min(sorted_list1,sorted_list2)) elements
        if list1[it_1] == list2[it_2]:
            merged_list.append(list1[it_1])
            it_1 += 1
            it_2 += 1
        elif list1[it_1] < list2[it_2]:
            it_1 += 1
        else:
            it_2 += 1

    return merged_list


def or_merge(sorted_list1, sorted_list2):
    merged_list = []
    # first we make copies of the lists, so we don't modify the existing lists in the index:
    list1 = list(sorted_list1)
    list2 = list(sorted_list2)

    for id in list1: merged_list.append(id)

    for id in list2:
        if id in merged_list: continue
        
        merged_list.append(id)

    return merged_list



def and_query(query, index, docs=None):
	if docs is None:	#supporting function - defining docs default paramenter as list caused some weird behaviour where the variable was saved when you called the function again for some reason
		docs = []

	if type(query) == str:		#initial state where query is a string
		query = normalizer(tokenizer(query))
		docs.extend(index[query[0]]) #fill docs with documnts that include only the first term to be able to compare with something later one in the recursion

	if len(query) <= 1:  #'bottom" of recursion where there's only one term left
		return and_merge(docs,index[query[0]])
	else:
		docs = and_merge(docs, index[query[0]]) #find common docs between already found document and documets including the next term - for the firt 'iteraion' docs and the term are the same documents

		return and_query(query[1:], index, docs) #run and_query again with all the query exluding the current first term

def or_query(query, index, docs=None):
	if docs is None:
		docs = []

	if type(query) == str:		#initial state where query is a string
		query = normalizer(tokenizer(query))
		docs.extend(index[query[0]]) #fill docs with documnts that include only the first term to be able to compare with something later one in the recursion

	if len(query) <= 1:  #'bottom" of recursion where there's only one term left
		return or_merge(docs,index[query[0]])	
	else:
		docs = or_merge(docs, index[query[0]]) #find common docs between already found document and documets including the next term - for the firt 'iteraion' docs and the term are the same documents

		return or_query(query[1:], index, docs) 
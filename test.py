from collections import defaultdict


lame = defaultdict(set)

lame['new'] = defaultdict(set)

lame['new'][1] = [4,4,2]
lame['new'][2] = [2,4,5]
print(lame)

# {1: ['new', 'home', 'sale', 'top', 'forecast', 'new'], 2: ['home', 'sale', 'rise', 'in', 'july'], 3: ['increase', 'in', 'home', 'sale', 'in', 'july'], 4: ['july', 'new', 'home', 'sale', 'rise'], 5: ['breakthrough', 'drug', 'for', 'schizophrenia'], 6: ['new', 'schizophrenia', 'drug'], 7: ['new', 'approach', 'for', 'treatment', 'of', 'schizophrenia', 'new', 'hope', 'for', 'schizophrenia', 'patient'], 8: ['the', 'inventor', 'stanford', 'ovshinsky', 'never', 'went', 'to', 'university'], 9: ['jonathan', 'went', 'to', 'stanford', 'university', 'last', 'year']}
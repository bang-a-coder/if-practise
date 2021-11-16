from collections import defaultdict


lame = defaultdict(set)

lame['new'] = defaultdict(set)

lame['new'][1] = [4,4,2]
lame['new'][2] = [2,4,5]
print(lame['new'])
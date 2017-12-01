#!/usr/bin/python

string_tri = []
string_dict_tri = []
with open('triphones1', 'r') as f:
	for line in f:
		string_tri.append(line.strip('\n'))

with open('dict-tri', 'r') as f:
	for line in f:
		done = False
		sss = line.strip('\n').split(' ')
		for ss in sss:
			if not done:
				done = True
				continue
			if ss == '': continue
			elif ss[0].isupper(): continue
			else: string_dict_tri.append(ss)

towrite = []

filetriph = open('triphones1', 'r')
for line in filetriph:
	towrite.append(line)

filetriph.close()

string_dict_tri = list(set(string_dict_tri)) 
for dicts in string_dict_tri:
	if dicts not in string_tri:
		print dicts
		towrite.append(dicts + '\r\n')

newfiletriph = open('triphones1', 'w')
for line in towrite:
	newfiletriph.write(line)

newfiletriph.close()


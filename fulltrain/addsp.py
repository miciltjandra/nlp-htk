import os

filehmm3 = file('hmm3/hmmdefs', 'r')
filehmm4 = file('hmm4/hmmdefs', 'w')

tocopy = []
startcopy = False

for line in filehmm3:
	filehmm4.write(line)
	if '"sil"' in line:
		startcopy = True
	if startcopy:
		tocopy.append(line)


startwrite = False

for line in tocopy:
	if startwrite:
		filehmm4.write(line)
		if 'GCONST>' in line:
			startwrite = False
			filehmm4.write('<TRANSP> 3\n')
			filehmm4.write(' 0.0 1.0 0.0\n')
			filehmm4.write(' 0.0 0.9 0.1\n')
			filehmm4.write(' 0.0 0.0 0.0\n')
			filehmm4.write('<ENDHMM>\n')
	if 'sil' in line:
		filehmm4.write('~h "sp"\n')
		filehmm4.write('<BEGINHMM>\n')
	elif 'NUMSTATES>' in line:
		filehmm4.write(line[:-2] + '3\n')
	elif 'STATE>' in line:
		if '3' in line:
			filehmm4.write(line[:-2] + '2\n')
			startwrite = True


filehmm4.close()

filemac3 = file('hmm3/macros', 'r')
filemac4 = file('hmm4/macros', 'w')

for line in filemac3:
	filemac4.write(line)

filemac4.close()
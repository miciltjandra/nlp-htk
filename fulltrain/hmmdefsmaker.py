filemono = open('monophones0', 'r')
fileproto = open('hmm0/proto', 'r')
filevfloor = open('hmm0/vFloors', 'r')

hmmdefs = open('hmm0/hmmdefs', 'w')
macros = open('hmm0/macros', 'w')

proto = []
hmm = []
monophones = []
record = False
for line in fileproto:
	proto.append(line)

for line in proto:
	if line == '<BEGINHMM>\n':
		record = True
	if record:
		hmm.append(line)
	if line == '<ENDHMM>\n':
		record = False

for line in filemono:
	monophones.append(line)

for phone in monophones:
	hmmdefs.write('~h "' + phone[:-1] + '"\n')
	for line in hmm:
		hmmdefs.write(line)

hmmdefs.close()

for idx, line in enumerate(proto):
	if idx < 3:
		macros.write(line)

for line in filevfloor:
	macros.write(line)

macros.close()

filehvite = open('HVite_log', 'r')
filetrain = open('train.scp', 'r')

hvite = []
for line in filehvite:
	if 'Aligning File: ' in line:
		nama = line
	elif line == 'No tokens survived to final node of network\n':
		hvite.append(nama[32:])

for line in hvite:
	print (line[:-1])


trainscp = []
for line in filetrain:
	found = False
	for item in hvite:
		if item[:-1] in line:
			found = True
		
	if not found:
		trainscp.append(line)
		found = False
	else:
		print line

filetrain.close()

newfiletrain = file('train.scp', 'w')
for line in trainscp:
	newfiletrain.write(line)

newfiletrain.close()

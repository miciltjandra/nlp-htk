import os

filerecout = file('recout.mlf', 'r')
fileout = file('out.mlf', 'w')

for line in filerecout:
	if not (('SENT-END' in line) or (' p ' in line)):		
		fileout.write(line)
	else:
		print line[:-1]

fileout.close()


#!/usr/bin/python
import sys

try:
	sys.argv[2]
except NameError:
	print('there is no file to output results')
else:
	mt = sys.argv[2] + 'mt.txt'	
	human = sys.argv[2] + 'human.txt'
	print (human);

try:
	training = open(sys.argv[1], 'r+')
	mttraining = open(mt, 'w+')
	humantraining = open(human, 'w+')
except IOError:
        print('cannot open file')
else:
	for line in training:
		if line:
			if line.startswith('0'):
				mttraining.write(line)
			elif line.startswith('1'):
				humantraining.write(line)
			else:
				print('invalid line for training')
		else:
			print('invalid line for training')
		






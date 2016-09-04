#! /usr/bin/env python3

## a script to add identifying OTU numbers to my otu clusters, which were an 
## output of usearch -cluster_smallmem program. 

## files should be in fasta format, will be outputted as a fasta

## user gives name of original file without otu labels, string for labels 
## (usually just 'OTU'), and name of output file.

from sys import argv
import re

script, otuin, tag, otuout = argv

num = 1

with open (otuin, 'r') as input:
	with open (otuout, 'w') as output:
		for i in input:
			if re.search ('\>', i): 
				line = i[0] + tag + str(num) + ':' + i[1:]
				#line = i.rstrip('\n') + tag + str(num) + '\n'
				num += 1
			else: line = i
			output.write(line)






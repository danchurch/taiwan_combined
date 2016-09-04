#! /usr/bin/env python3

## a script to remove all sequences from UNITE database that have class or higher 
## unindentified 

## this version is written for UNITE database for usearch8.1 -utax: see https://unite.ut.ee/repository.php


from sys import argv

import re

script, fasta_in, fasta_out = argv

rit = 0

with open (fasta_in, 'r') as input:
	with open (fasta_out, 'w') as output:
		header = ''
		seq = ''
		for h in input:
		## if it's a header with class-level ID, save it:
			if re.search ('\>', h) and re.search (',c:.+', h): 
				header = h
		## if it's a sequence and there's a header from previous line, print the head and the sequence
			elif  not re.search('[a-z]', h) and header != '':
				seq = h
				output.write(header)
				output.write(seq)
				header=''
				seq=''




#! /usr/bin/env python3

## make a script to get multiline fastas back to two-line fastas

from sys import argv
import re

script, fasta_in, fasta_out = argv

line = ''
firstline=1

with open(fasta_in, 'r') as multfa:
	with open(fasta_out, 'w') as regfa:

		for h in multfa:
			## if it's the first line, write it:
			if firstline == 1 and re.search('\>',h):
				line=h
				firstline=0
			## if not, and we find a header, add line break and print existing 'line', then dump it and grab header:
			elif re.search('\>',h):
				line += '\n'
				regfa.write(line)
				line=h
			## if line has nucleotides, add this to the 'line' variable:
			elif re.search('[GCATN]',h) and not re.search('\>',h):
				line += h.rstrip('\n')
		## finish off the last read:
		line += '\n'
		regfa.write(line)

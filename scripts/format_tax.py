#! /usr/bin/env python3

## script to take taxonomy metadata from a usearch-created biome, and reformat
## to look more like what I think biom wants.

from sys import argv
import re

script, biomin, biomout = argv

with open (biomin, 'r') as input:
	with open (biomout, 'w') as output:
		for i in input:
			if re.search ('\"taxonomy\":\"d:Fungi\(', i):
				## change taxonomic level symbols:
				i=re.sub('"d:Fu', ' ["k__Fu', i)
				i=re.sub(',p:','", "p__', i)
				i=re.sub(',c:','", "c__', i)
				i=re.sub(',o:','", "o__', i)
				i=re.sub(',f:','", "f__', i)
				i=re.sub(',g:','", "g__', i)
				i=re.sub(',s:','", "s__', i)
				## add end bracket
				i=re.sub('}}', ']}}',i)
				## get rid of parethenses:
				i=re.sub('\([0-1]?\.[0-9]*\)','', i)

			output.write(i)



## for non-comma separation. Almost works?
#
#with open (biomin, 'r') as input:
#	with open (biomout, 'w') as output:
#		for i in input:
#			if re.search ('\"taxonomy\":\"d:Fungi\(', i):
#				## change taxonomic level symbols:
#				i=re.sub('"d:Fu', ' "Root;k__Fu', i)
#				i=re.sub(',p:',';p__', i)
#				i=re.sub(',c:',';c__', i)
#				i=re.sub(',o:',';o__', i)
#				i=re.sub(',f:',';f__', i)
#				i=re.sub(',g:',';g__', i)
#				i=re.sub(',s:',';s__', i)
#				## get rid of parethenses:
#				i=re.sub('\([0-1]?\.[0-9]*\)','', i)
#
#			output.write(i)
#

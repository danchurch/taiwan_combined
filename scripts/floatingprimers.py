#! /usr/bin/env python3

## make a script that removes any forward, reverse, or reverse complement primers from our reads
## note that so far, my best efforts to make this script regex compliant have failed, so it does
## not get rid of degenerate copies of the primers, of which there are possibly several hundred 
## in my dataset

## make sure that primers in their proper places have already been removed

## use on fasta or fna files, not fastq

from sys import argv 
import re 

script, seqs, out_put, forwardpr, reversepr = argv 

def revcompl(x): 
	aa=''.join([{'A':'T','C':'G','G':'C','T':'A','N':'N','.':'.'}[B] for B in x][::-1])
	return(aa)

with open (seqs, 'r') as input:
	with open(out_put, 'w') as output:
		prevline=''
		for h in input:
			if not (re.search(forwardpr, h) or re.search(reversepr, h) or re.search(revcompl(forwardpr), h) or re.search(revcompl(reversepr), h) or '>' in h):

				output.write(prevline)
				output.write(h)
			prevline = h

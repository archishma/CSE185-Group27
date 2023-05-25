### BWDTools Main File 
### Archishma Kavalipati, Allexa Remigio, Iris Lee 
### CSE 185 Spring 2023 

import sys
import os 
import gzip 

def process_input(infile):
    '''Takes in a VCF file and processes the input.'''
    fileformat = ''
    source = '' 
    variant_lines = [] # stores each line of the vcf in a list of lists 
    with gzip.open(infile, mode='rt') as f:
        for line in f:
            if '##fileformat' in line:
                fileformat = line.split('=')[1].strip()
            elif '##source' in line:
                source = line.split('=')[1].strip()
            elif '##' not in line:
                processed = line.split()
                variant_lines.append(processed)
            else:
                pass
    return(variant_lines, fileformat, source) 

def index(variant_lines):
    '''Takes in variant lines and outputs the number of variants.'''
    # currently the first line is just the header, I will edit this very rough code later
    # that is why I subtract 1 from the length 
    return(len(variant_lines) - 1)
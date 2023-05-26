### BWDTools Main File 
### Archishma Kavalipati, Allexa Remigio, Iris Lee 
### CSE 185 Spring 2023 

import sys # for taking in command-line arguments eventually 
import gzip # for working with gzipped data, as most VCF files are in the format *.vcf.gz

def process_input(infile):
    '''Takes in a VCF file and processes the input. This is the first step run before any BWDTools operations are run. '''
    fileformat = ''
    source = '' 
    header = []
    variant_lines = [] # stores each line of the vcf in a list of lists 
    with gzip.open(infile, mode='rt') as f:
        for line in f:
            if '##fileformat' in line:
                fileformat = line.split('=')[1].strip()
            elif '##source' in line:
                source = line.split('=')[1].strip()
            elif '#CHROM' in line:
                header = line.split()
            elif '##' not in line:
                processed = line.split()
                variant_lines.append(processed)
            else:
                pass
    return(variant_lines, header, fileformat, source) 

def num_variants(variant_lines):
    '''Takes in variant lines and outputs the number of variants.'''
    return(len(variant_lines))

def list_samples(header):
    '''Returns a list of the samples in the VCF file.'''
    samples = ''''''
    for i, s in enumerate(header[9:]):
        samples += s
        if i != len(header[9:]) - 1: # fix later 
            samples += '\n'
    return samples
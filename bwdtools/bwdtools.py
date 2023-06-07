### BWDTools Main File 
### Archishma Kavalipati, Allexa Remigio, Iris Lee 
### CSE 185 Spring 2023 

import argparse # for taking in command-line arguments 
import sys # for working with command-line arguments 
import gzip # for working with gzipped data, as most VCF files are in the format *.vcf.gz

parser = argparse.ArgumentParser(prog ='BWDTools')

parser.add_argument('vcf', help='Path to VCF file to be processed.')
parser.add_argument('-v', '--num-variants', action='store_true', help='List the number of variants in the VCF file.')
parser.add_argument('-s', '--list-samples', action='store_true', help='List the samples in the VCF file.')
# making qid argument group mutually exclusive from other arguments
mu = parser.add_mutually_exclusive_group(required=False)
mu.add_argument('-qid', type=str, help='List the position or range of allele') #see 'by_pos() --> args.qid = positions'

args = parser.parse_args()

def process_input(infile):
    '''Takes in a VCF file and processes the input. 
    This is the first step run before any BWDTools operations are run. '''
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

def by_pos(positions, variant_lines):
    variants = []
    if '-' in positions:
        start, end = int(positions.split('-')[0]), int(positions.split('-')[1])
        for line in variant_lines:
            if int(line[1]) >= start and int(line[1]) <= end:
                variants.append(line)
    
    else:
        pos = int(positions)
        for line in variant_lines:
            if int(line[1]) == pos:
                variants.append(line)
    return variants 

### MAIN METHODS
if __name__ == '__main__':
    if len(sys.argv) == 2: # no optional arguments were provided 
        sys.exit('Error: no options provided! Use -h or --help for usage.')
    if "vcf.gz" not in args.vcf:
        sys.exit('Error: incorrect vcf input provided! Usage supports vcf.gz files.')
    # Process the input 
    infile = args.vcf
    variant_lines, header, fileformat, source = process_input(infile)
    if args.qid:
        qid_variant_lines = by_pos(args.qid, variant_lines)
        if args.num_variants:
            print(num_variants(qid_variant_lines))
    else:
        if args.num_variants:
            print(num_variants(variant_lines))
    if args.list_samples:
        print(list_samples(header))
    else:
        pass

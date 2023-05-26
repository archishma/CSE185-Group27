# CSE185-Group27: BWDTools
CSE 185 Spring 2023 Project
BWDTools (a.k.a BCFtools Walmart Dupe)

## Description
Compared to the BCFtools options "index" and "query", BWDtools finds all variants in a sample VCF file and create a list of all the samples. This tool can be implemented on the entire sample or from specific regions of the input file, similar to the BFCtools "-r" flag options.

## Usage
`python bwdtools.py <input_file>`

Component | Definition 
 ------------ | ------------- 
bwdtools.py | the main file to execute for processing and indexing the input file
<input_file>  | vcf file

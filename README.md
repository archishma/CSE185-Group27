# CSE185-Group27: BWDTools
CSE 185 Spring 2023 Project
BWDTools (a.k.a BCFtools Walmart Dupe)

## Authors
Archishma Kavalipati, Allexa Remigio, Iris Lee

CSE 185 SP23 Project Creator: Melissa Gymrek 

## Status
Completed

## Description
Compared to the BCFtools options "index" and "query", BWDTools locates all the variants in a sample VCF file, then generates a list of all the samples. This tool can be implemented on the entire sample or from specific regions of the input file, similar to the BFCtools "-r" flag options, and outputs to the local terminal.

## Installation
In order to utilize BWDTools, please use run the following command in your terminal to install the `bwdtools` program:

`pip install bwdtools`

## Usage/Options
`python bwdtools.py <input_file> stats ( -qid <allele_position> )| -s | -v ( -qid <allele_position> ) `

There is the option to have the overall stats summary of the entire file, only look at a certain allele position, or a range of positions.

Component | Definition 
 ------------ | ------------- 
bwdtools.py | the main file to execute for processing and indexing the input file
<input_file>  | input vcf file (must already be indexed and in format **.vcf.gz*)
stats  | to output simple summary of stats (frequency of unique IDs, alleles, number of variants, and list) 
-samples  | option to print the sample list
-variants  | option to print the number of variants
-qid  | option to select a specific allele position/interval (functions only with -v option)
<allele_position>  | Position/Range of allele (i.e. 128419307 or 128419307-128421762)

Options `stats` and `v` can *optionally* be utilized over a certain allele position or interval.


## Sample Commands
Using the sample file "trio.vcf.gz" from the "vcf" directory, we can print a list of its samples using the `-s` option:
```
python bwdtools.py ~/vcf/trio.vcf/gz -s
```
Output:
```
List of All Samples:
Sample 1
Sample 2
Sample 3
```
We can also use the `-v` option to print the number of variants in the same VCF file:
```
python bwdtools.py ~/vcf/trio.vcf.gz -v
```
Output:
```
Number of all Variants: 50
```
To output a simple summary of the VCF file, we can use the `stats` option:
```
python bwdtools.py ~vcf/trio.vcf/gz stats
```
Output:
```
Number of Variants :  50
Unique ID frequency:  {'.': 50}
Unique Alleles and frequencies:

Allele: C, Frequency: 1
```

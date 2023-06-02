# CSE185-Group27: BWDTools
CSE 185 Spring 2023 Project
BWDTools (a.k.a BCFtools Walmart Dupe)

## Authors
Archishma Kavalipati, Allexa Remigio, Iris Lee

CSE 185 SP23 Project Creator: Melissa Gymrek 

## Status
Incomplete for the following:
- Installation
- BWDTools Options

## Description
Compared to the BCFtools options "index" and "query", BWDtools locates all the variants in a sample VCF file, then generates a list of all the samples. This tool can be implemented on the entire sample or from specific regions of the input file, similar to the BFCtools "-r" flag options.

## Installation
*The tool is not yet suited for installation. This will be updated at a future date. Therefore, BWDTools can only be run locally through python at the moment.*

In order to utilize BWDTools, please use run the following command in your terminal to install the `bwdtools` library:

`pip install bwdtools`

## Usage/Options
`python bwdtools.py <input_file> | -qid <allele_position> `

There is the option to have the overall stats summary of the entire file, only look at a certain allele position, or a range of positions.

Component | Definition 
 ------------ | ------------- 
bwdtools.py | the main file to execute for processing and indexing the input file
<input_file>  | input vcf file
<allele_position>  | Position/Range of allele (i.e. 128419307 or 128419307-128414945)
<!--stats  | to output summary of stats (frequency of unique IDs and alleles)  i took this out for now-->


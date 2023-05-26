import bwdtools
from subprocess import Popen, PIPE 

testfile = '/home/akavalip/teams/27/vcf/child.vcf.gz'
testfile2 = '/home/akavalip/teams/27/vcf/trio.vcf.gz' # the trio vcf file from lab 1 

### testing how process_input works 
flines, fheader, fformat, fsource = bwdtools.process_input(testfile)
print('File header: ' + str(fheader))
print('File format: ' + str(fformat))
print('File format: ' + str(fsource))

### test how the num_variants function works 
process = Popen(['bcftools', 'index', '-n', testfile], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

if bwdtools.num_variants(flines) == int(stdout): # the number of variants from `bcftools index -n`
    print('Function `num_variants`: pass')
else:
    print('Error in number of variants!')
    
### test how list_samples function works 
flines, fheader, fformat, fsource = bwdtools.process_input(testfile2)
print(bwdtools.list_samples(fheader))

process = Popen(['bcftools', 'query', '-l', testfile], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

if bwdtools.list_samples(fheader) == stdout: # the lines from `bcftools query -l`
    print('Function `list_samples`: pass')
else:
    print('Error in list of samples!')
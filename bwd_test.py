import bwdtools

### testing how process input works 
flines, fformat, fsource = bwdtools.process_input('/home/akavalip/teams/27/vcf/child.vcf.gz')
# print(flines)
print(fformat, fsource)
print(len(flines))

### test how the index function works 
assert bwdtools.index(flines) == 37
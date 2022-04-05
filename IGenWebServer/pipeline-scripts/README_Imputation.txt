Reference files needed: 
1000GP_Phase3 folder 
Phase_References folder 
Homo_sapiens.GRCh37.75.dna.primary_assembly.fa
Homo_sapiens.GRCh37.75.dna.primary_assembly.fa.fai 

Tools needed: 
eagle2 -- not in conda 
gtool -- not in conda 
plink
impute2 
bcftools 
vcftools 
bgzip -- should be in bin folder 
tabix -- should be in bin folder 

inputfiletype.sh
three inputs needed: file type (1st input) file name (2nd input) outputfolderpath (3rd input)
This script will convert the input file to 23andMe format and call masterscript.sh

masterscript.sh
two inputs needed: file name (in 23andMe format) and outputfolderpath
calls three scripts: imputation_pipeline.py, impute2temp.py, temp2vcf.sh

imputation_pipeline
two inputs needed: file name (in 23andMe format) and outputfolderpath
Threading is hardcoded, but you can change the number of threads in inputefiletype.sh
output: gen file 

impute2temp.py 
two inputs needed: file name (in 23andMe format) and outputfolderpath
concatenates impute files by chromosome, extracts rsids from each file, filters file to only include lines with rsids 

temp2vcf.py 
two inputs needed: file name (in 23andMe format) and outputfolderpath
takes imputed filtered files and outputs a singular vcf for PRS calculation 



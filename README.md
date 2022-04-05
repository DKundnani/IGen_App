# IGen - Infection Genetics 
### An app that can give you relative risk estimates for multiple common infections by looking at your personal genome from different Direct To Consumer genetic testing companies

Check out our website application! http://team2.bioapp208803.biosci.gatech.edu/login/

#### Dependencies
Conda enviroment: 

VCftools, Bcftools, Plink, Eagle=v..
Python >3.5 pip libraries: pandas, Numpy, Scipy
openssl=v1.0.2

#### Pipeline

![iGen_Final_Pipeline](https://github.gatech.edu/storage/user/43860/files/7aa4a000-5d78-11eb-8095-c328d5b1c755)

#### Merging subject vcf file to the 1000 Genomes Reference Dataset (Before Imputation for PCA and Population Stratification, After Imputation for PRS Score Calculations)

merge.py -

#### Imputation
Phasing and imputing the subject vcf file from 23andMe, Ancestry, or FTDNA

imputation_pipeline.py - 

#### PCA 
Using 1000 Genomes Reference DNA and input subject vcf file to create a PCA for determining user ancestry 

PCA.sh - 
KNN.py -

#### List of Infections
Chicken pox, Shingles, Cold sores, Mononucleosis, Mumps, Hepatitis B, HIV, TB, Strep throat, Yeast Infections, Childhood ear infections


#### From Imputed Vcf file to Getting the PRS scores
Extracting SNPs from the imputed subject vcf file pertaining to the Infections we are interested in
merge.py -

Generating PRS Score has follwoing two steps:
1. Getting Valid SNPs for every Infection by Clumping and Threshold using Plink
1. Getting PRS score for every Infection using the above Valid SNPs

PRS.py -

#### Percentile Calculation

percentile.py -

#!/bin/bash

#first argument is unique output location 

bgzip ${1}/PCA_merge/merged.vcf 
tabix ${1}/PCA_merge/merged.vcf.gz

mkdir ${1}/PCA

plink --vcf ${1}/PCA_merge/merged.vcf.gz --make-bed --pca --out ${1}/PCA/1000G_PCA_merged 

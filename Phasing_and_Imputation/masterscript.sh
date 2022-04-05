#!/bin/bash


python3 imputation_pipeline.py -i $1 -t $2 -d $3

python3 impute2temp.py -i $1 -d $3

./temp2vcf.sh $1 -d $3

 

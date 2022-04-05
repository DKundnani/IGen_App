#!/bin/bash 

#first argument is user ID - must be in 23and me format from the inputfiletype.sh
#second argument is unique output location 



python3 merge.py -r 1000G.vcf -t ${2}/${1}_noduplicates.vcf -o ${2}/PCA_merge -c ${1}

./PCA.sh ${2}

python3 KNN.py -d ${2}




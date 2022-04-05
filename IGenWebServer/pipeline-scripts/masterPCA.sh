#!/bin/bash 

#first argument is user ID - must be in 23and me format from the inputfiletype.sh
#second argument is unique output location 

cd /projects/team-2/html/biol-8803-IGen/IGenWebServer/pipeline-scripts

gunzip ${2}/inputfile_filtered.gz
python3 merge.py -r /projects/team-2/html/1000G.vcf -t ${2}/inputfile_filtered -o ${2}/PCA_merge -c ${1}

./PCA.sh ${2}

python3 KNN.py -d ${2}




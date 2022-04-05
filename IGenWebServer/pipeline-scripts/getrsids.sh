#!bin/bash

awk 'BEGIN{while((getline<"rsids.txt")>0)l[$1]=1}/^#/||l[$3]' $1 > $2
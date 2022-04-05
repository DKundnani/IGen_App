#!/bin/bash 

cat ${3}/imputetemp/${1##*/}-2_impute_filtered | awk '{split($2,a,":"); $2="2:"a[2]"_"a[3]"_"a[4]; print $1,$2,$3,$4,$5}' > ${3}/imputetemp/${1##*/}-2_awk.gen

#cat ${3}/imputetemp/${1##*/}-3_impute_filtered | awk '{split($2,a,":"); $2="3:"a[2]"_"a[3]"_"a[4]; print $1,$2,$3,$4,$5}' > ${3}/imputetemp/${1##*/}-3_awk.gen
#cat ${3}/imputetemp/${1##*/}-6_impute_filtered | awk '{split($2,a,":"); $2="6:"a[2]"_"a[3]"_"a[4]; print $1,$2,$3,$4,$5}' > ${3}/imputetemp/${1##*/}-6_awk.gen
#cat ${3}/imputetemp/${1##*/}-7_impute_filtered | awk '{split($2,a,":"); $2="7:"a[2]"_"a[3]"_"a[4]; print $1,$2,$3,$4,$5}' > ${3}/imputetemp/${1##*/}-7_awk.gen
#cat ${3}/imputetemp/${1##*/}-8_impute_filtered | awk '{split($2,a,":"); $2="8:"a[2]"_"a[3]"_"a[4]; print $1,$2,$3,$4,$5}' > ${3}/imputetemp/${1##*/}-8_awk.gen
#cat ${3}/imputetemp/${1##*/}-12_impute_filtered | awk '{split($2,a,":"); $2="12:"a[2]"_"a[3]"_"a[4]; print $1,$2,$3,$4,$5}' > ${3}/imputetemp/${1##*/}-12_awk.gen
#cat ${3}/imputetemp/${1##*/}-17_impute_filtered | awk '{split($2,a,":"); $2="17:"a[2]"_"a[3]"_"a[4]; print $1,$2,$3,$4,$5}' > ${3}/imputetemp/${1##*/}-17_awk.gen
#cat ${3}/imputetemp/${1##*/}-19_impute_filtered | awk '{split($2,a,":"); $2="19:"a[2]"_"a[3]"_"a[4]; print $1,$2,$3,$4,$5}' > ${3}/imputetemp/${1##*/}-19_awk.gen


for file in ${3}/imputetemp/*impute_filtered*;
do
echo $file
useridchr=${file##*/}
useridchr=${useridchr%%_*}
chr=${useridchr##*-}
userid=${useridchr%%-*}

gzip ${3}/imputetemp/${useridchr}_awk.gen 


bcftools convert --gensample2vcf ${3}/imputetemp/${useridchr}_awk > ${3}/imputetemp/${useridchr}_imputed.vcf

sed "/#/d" ${3}/imputetemp/${useridchr}_imputed.vcf > ${3}/imputetemp/${useridchr}_nohash.vcf

paste ${3}/imputetemp/${useridchr}_nohash.vcf ${3}/imputetemp/rsidfile${chr} ${3}/imputetemp/genotypeinfo${chr} | awk '{print $1"\t"$2"\t"$9"\t"$4"\t"$5"\t"$6"\t"$7"\t"$7"\t"$7"\t"$12}' > ${3}/imputetemp/${useridchr}_rsid.vcf

done
grep "#" ${3}/imputetemp/${userid}-2_imputed.vcf > ${3}/imputetemp/${userid}-2_header.vcf

sed 's/$/\tFORMAT\tsample/' ${3}/imputetemp/${userid}-2_header.vcf > ${3}/imputetemp/${userid}-2_headerfinal.vcf

#cat ${3}/imputetemp/${userid}-2_headerfinal.vcf ${3}/imputetemp/${userid}-2_rsid.vcf ${3}/imputetemp/${userid}-3_rsid.vcf ${3}/imputetemp/${userid}-6_rsid.vcf ${3}/imputetemp/${userid}-7_rsid.vcf ${3}/imputetemp/${userid}-8_rsid.vcf ${3}/imputetemp/${userid}-12_rsid.vcf ${3}/imputetemp/${userid}-17_rsid.vcf ${3}/imputetemp/${userid}-19_rsid.vcf > ${3}/${userid}_final.vcf

cat ${3}/imputetemp/${userid}-2_headerfinal.vcf ${3}/imputetemp/${userid}-2_rsid.vcf > ${3}/${userid}_final.vcf

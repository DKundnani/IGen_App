#!/bin/bash 

#23andme file 
prefix=${2%%.*}
prefix=${prefix//[^[:alnum:]]/}

mkdir ${3}/eagleoutput
mkdir ${3}/imputeoutput

if  [[ $1 == 23andme ]];
then
	./masterscript.sh $2 3 $3;
fi 

#FTDNA file 
if [[ $1 == FTDNA ]];
then 
cat $2 | grep "rs[0-9]" | sed -e 's/,/\t/g' -e '/seq/d' -e '/--/d' -e '/0\t0/d' > ${prefix}23format
./masterscript.sh ${prefix}23format 3 $3
fi 

if [[ $1 == Ancestry ]];
then 
sed "/#/d" $2 > ${prefix}_nohash

grep "#" $2 > ${prefix}_header

cat ${prefix}_nohash | awk '{print $1"\t"$2"\t"$3"\t"$4$5}'> ${prefix}_temp

cat ${prefix}_header ${prefix}_temp >${prefix}23format
rm ${prefix}_nohash ${prefix}_header ${prefix}_temp

./masterscript.sh ${prefix}23format 3 $3
fi


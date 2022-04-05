#!/usr/bin/env python3
import argparse
import subprocess
import re 
from multiprocessing import Pool

parser=argparse.ArgumentParser()
parser.add_argument("-i", required=True)
parser.add_argument("-d")
args=parser.parse_args()

subprocess.call(["rm", "-r", args.d + "/imputetemp/"])
subprocess.call(["mkdir", args.d + "/imputetemp/"])

def openfile(filename, chr):
	tempoutput=open(args.d + "/imputetemp/" + args.i + "-" + str(chr) + "_impute_filtered", "a")
	rsidfile=open(args.d + "/imputetemp/rsidfile" + str(chr), "a")
	genotypeinfo=open(args.d + "/imputetemp/genotypeinfo" + str(chr), "a")
	with open(args.d + "/imputeoutput/" + filename, "r") as fh:
		for line in fh:
			if line.startswith("--- rs"):
				tempoutput.write(line)
				line=line.strip("\n")
				row=line.split(" ")
				row[1]=row[1].split(":")
				rsidfile.write(row[1][0] + "\t" + row[1][1] + "\n")
				genotype=row.index(max(row[5], row[6], row[7]))
				if genotype==5:
					genotypeinfo.write(row[1][0] + "\t" + "0/0" + "\n")
				if genotype==6:
					genotypeinfo.write(row[1][0] + "\t" + "0/1" + "\n")
				if genotype==7:
					genotypeinfo.write(row[1][0] + "\t" + "1/1" + "\n")

openfile(args.i + "_impute2_1", 2)
openfile(args.i + "_impute2_2", 2)
openfile(args.i + "_impute3_3", 3)
openfile(args.i + "_impute3_4", 3)
openfile(args.i + "_impute7_106", 7)
openfile(args.i + "_impute7_107", 7)
openfile(args.i + "_impute8_108", 8)
openfile(args.i + "_impute8_109", 8)
openfile(args.i + "_impute12_110", 12)
openfile(args.i + "_impute17_111", 17)
openfile(args.i + "_impute19_112", 19)
openfile(args.i + "_impute19_113", 19)

for i in range(5, 106):
	openfile(args.i + "_impute6_" + str(i), 6)

chrlist=[2,3,6,7,8,12,17,19]
for chr in chrlist:			
	sampleoutput=open(args.d + "/imputetemp/" + args.i + "-" + str(chr) + "_awk.samples", "w")
	sampleoutput.write(args.i)


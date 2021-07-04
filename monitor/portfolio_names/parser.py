import os
import csv


tsv_file = open("dow30")
read_tsv = csv.reader(tsv_file, delimiter="\t")

dow30 = []

# read_tsv.readline()
for row in read_tsv:
  print(row[0].strip('\n'))
  dow30.append(row[0])

print(len(dow30))
#!/bin/bash
input="listtotest.txt"
while IFS= read -r var
do
  python new_cli.py sanjay.bont@gmail.com google123 $var LUTT.csv
done < "$input"

python filter.py LUTT.csv LUTT-filtered.csv
read year
#!/bin/bash
#exiftool aggregation script, made to quickly help with my penetration testing class assignment
#gets the output of exiftool on each file in the current directory and puts that into a text file
#then takes all of the text files in the directory and combines unique fields into a final text file to see
#any interesting things, which could then be found through various commands to search all text files in the
#current directory 
for FILE in * 
do
exiftool $FILE > $FILE.txt
cat $FILE.txt
echo -e "\n"
done;
cat *.txt > metadata.txt
sort -u metadata.txt > unique_metadata.txt
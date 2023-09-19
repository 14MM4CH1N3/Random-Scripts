#!/bin/bash
#downloads list of links into current directory
#puts the url as the title with substituted characters for ones that can't be filenames
filename="links.txt"
while read -r url; do
    output_filename=$(echo "$url" | sed 's/[^a-zA-Z0-9]/_/g')
    wget -O "$output_filename" "$url"
    sleep 1
done < "$filename"
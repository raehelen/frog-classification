#!/bin/bash
for filename in positive/*.jpg; do

	echo $filename
# 	convert "$filename" -resize x1600 "$filename"
	convert "$filename" -resize 33% "$filename"
done
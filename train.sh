#! /bin/bash

##### SETTINGS ######
					#
width="180"			#
height="180"		#
					#
#####################

# # resize input images
# bash resize.sh
#
# # "compiling negatives list..."
# find ./negative -name '*.jpg' > negatives.txt
 
# launch annotation tool
# opencv_annotation --annotations=annotations.txt --images=positive/

# create vec file
opencv_createsamples -info annotations.txt -vec frogs.vec -w "$width" -h "$height"

rm -rf "$width x $height"
mkdir "$width x $height"

# train classifier
opencv_traincascade -data "$width x $height" -vec frogs.vec -bg negatives.txt -numStages 12 -numPos 8 -numNeg 540 -w "$width" -h "$height" -mode ALL #-precalcValBufSize 1024 -precalcIdxBufSize 1024

# launch test script
# python detect_frog.py -i test.jpg -c "$width x $height"/cascade.xml

echo "done"
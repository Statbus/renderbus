#!/bin/sh
for png in `find $1 -type f -name "*.png" -depth 1`;
do
	echo "crushing $png"	
	pngcrush "$png" temp.png
	mv -f temp.png $png
done;

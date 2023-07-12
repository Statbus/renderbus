#!/bin/bash

TILESIZE=256

mkdir -p $1/tiles

for fullrender in `find $1 -type f -name "*.png" -depth 1 -exec basename {} \;`;
do
    renderpath=$1/$fullrender
    mapname=${fullrender//'.png'/}
    ZOOM=5
    DESTDIR=$1/tiles/$mapname

	MAPSIZE=`identify -format "%w" $1/$fullrender`
	
	CROP="$TILESIZE"
	CROP+="x$TILESIZE"
	
	# #Run the first tile pass on the main map size WITHOUT resizing
	mkdir -p $DESTDIR/$ZOOM
	convert $1/$fullrender -crop $CROP +gravity -set filename:tile $DESTDIR/$ZOOM/tile_%[fx:page.x/$TILESIZE]-%[fx:page.y/$TILESIZE] %[filename:tile].png
	
	ZOOM=$[$ZOOM-1] #Since we're not resizing the first iteration, we skip a zoom level
	
	while [ $ZOOM -gt 0 ]
	do
	  MAPSIZE=$[$MAPSIZE/2]
	  RESIZE="$MAPSIZE"
	  RESIZE+="x$MAPSIZE"
	  mkdir -p $DESTDIR/$ZOOM
	  convert $1/$fullrender -resize $RESIZE -crop $CROP +gravity -set filename:tile $DESTDIR/$ZOOM/tile_%[fx:page.x/$TILESIZE]-%[fx:page.y/$TILESIZE] %[filename:tile].png
	
	ZOOM=$[$ZOOM-1]
	done
done
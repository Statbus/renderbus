# Renderbus
Render maps of tg- derived Space Station 13 codebases! _Now easier than ever!_

This uses docker, so you'll ned to have that installed.

## 1. First off, build SpacemanDMM:
IN THE PLACE WHERE YOU CLONED SPACEMANDMM:
```
docker build -t spacemandmm
```

This builds a SpacemanDMM docker image locally and tags it as `spacemandmm`.

## 2. Generate a list of maps to render

We're gonna grab a bunch of json files and parse them to generate our list of maps to render.

You can run this locally, or you can do what I do and use python via docker:

```
docker run -it --rm \
    -v tgstation/:/tg \
    -v $(pwd):/work:Z \
    -w /work \
    python:3 /work/getmaps.py /tg /output
```

This is gonna spit out a list of maps to feed to the renderer in step 3.

## 3. Next, render the maps:

We'll run the spacemandmm docker image we just built, with two volumes mounted: 
* The SS13 codebase you want to render maps from (update this yourself)
and
* The path to your output directory, which will by default be in this directory

```
docker run --rm \
    -v tgstation/:/tg \ 
    -v $(pwd)/output:/output \
    spacemandmm --env /tg/tgstation.dme \
    minimap /tg/_maps/map_files \
    -o /output
```
By itself, this command should spit out the help text. Copy the output from step 2 and paste it at the end of the command above, so you wind up with something like this: 

```
docker run -v tgstation-1:/tg -v $(pwd)/output:/output spacemandmm --env /tg/tgstation.dme minimap -o /output  /tg/_maps/map_files/Birdshot/birdshot.dmm /tg/_maps/map_files/Deltastation/DeltaStation2.dmm /tg/_maps/map_files/IceBoxStation/IceBoxStation.dmm /tg/_maps/map_files/MetaStation/MetaStation.dmm /tg/_maps/map_files/debug/multiz.dmm /tg/_maps/map_files/NorthStar/north_star.dmm /tg/_maps/map_files/debug/runtimestation.dmm /tg/_maps/map_files/tramstation/tramstation.dmm
```
(this will take a while)

## 4. Crush them as though they were your enemies
The resulting PNG files created by SpacemanDMM (~16mb) are huge. So we'll run 'em through pngcrush:

```
./crush.sh output/
```
(this will take _quite_ a while)
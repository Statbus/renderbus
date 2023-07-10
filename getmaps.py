#!/usr/bin/env python

import os, json
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description='Smush your codebase json mapfiles into one')
parser.add_argument('--codebase', metavar='N', type=str, nargs='?',
                    help='Path to your ss13 code repository')
parser.add_argument('--out_dir', metavar='N', type=str, nargs='?',
                    help='Path to output for the merged json')
args = parser.parse_args()

codebase = args.codebase
out_dir = args.out_dir
maps_dir = f"{codebase}/_maps"

maps = []
maplist = []

json_files = [pos_json for pos_json in os.listdir(maps_dir) if pos_json.endswith('.json')]

for j in json_files:
    maps.append(json.load(open(codebase+'/_maps/'+j)))

with open(f"{out_dir}/maps.json", 'w') as mapjson:
    json.dump(maps, mapjson)

for m in maps: 
    maplist.append(f"{maps_dir}/{m['map_path']}/{m['map_file']}")

print("\n")
print("\n")
print(" ".join(maplist))
print("\n")
print("\n")

#!/usr/bin/env python

import os, json
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Smush your codebase json mapfiles into one')
parser.add_argument('--codebase', metavar='N', type=str, nargs='?',
                    help='Path to your ss13 code repository')
parser.add_argument('--out_dir', metavar='N', type=str, nargs='?',
                    help='Path to output for the merged json')
args = parser.parse_args()


def get_git_revision_hash() -> str:
    return subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=codebase).decode('ascii').strip()

def get_git_revision_short_hash() -> str:
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], cwd=codebase).decode('ascii').strip()

def get_git_revision_date() -> str:
    return subprocess.check_output(['git', 'log', '-n1', '--pretty=%ci', 'HEAD'], cwd=codebase).decode('ascii').strip()

codebase = args.codebase
out_dir = args.out_dir
maps_dir = f"{codebase}/_maps"

revision = {}
revision['hash'] = get_git_revision_hash()
revision['shorthash'] = get_git_revision_short_hash()
revision['date'] = get_git_revision_date()

with open(f"{out_dir}/revision.json", 'w') as revisionjson:
    json.dump(revision, revisionjson)

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

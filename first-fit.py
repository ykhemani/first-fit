#!/usr/bin/python3

import argparse
from EnvDefault import env_default

version = '0.0.1'

parser = argparse.ArgumentParser(
  description = 'Use first fit decreasing algorithm for bin packing.'
)

parser.add_argument(
  '--rod_size',
  action=env_default('RODSIZE'),
  help='Rod size - e.g.: 20',
  required=True
)

parser.add_argument(
  '--segments',
  action=env_default('SEGMENTS'),
  help='List of segment lengths specified by a space - e.g.: 5 12 8 4 15 10',
  required=True
)

parser.add_argument(
  '--version',
  help='Version',
  action='version',
  version=f"{version}"
)

args = parser.parse_args()

#rod_size = 20
#segments = [5,12,8,15,15]
rods = []

#rod_size  = input("Enter the rod size (e.g. 20): ")
rod_size = int(args.rod_size)

#segments_input = input("Enter the segment sizes separated by spaces: ")
segment_split = args.segments.split()
segments = list(map(int, segment_split))

segments.sort(reverse=True)
print ()
print ("Segments: {}".format(segments))
print ("Rod size: {}".format(rod_size))
print ()

for segment in segments:
  #print("Looking for a spot for segment: {}".format(segment))
  if segment > rod_size:
    print("Error: Segment of length {} is too large for rod size {}.".format(segment, rod_size))
    continue

  found_a_rod = False
  for rod in rods:
    rod_sum = sum(rod)

    if (rod_sum + segment) <= rod_size:
      rod.append(segment)
      #print("{} - found a rod".format(segment))
      found_a_rod = True
      break

  if found_a_rod:
    continue

  rods.append([segment])
  #print("{} - created new rod".format(segment))

print ("Rods:")
for rod in rods:
  print(rod)

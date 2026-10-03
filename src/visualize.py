#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# keep the top 10 keys and sort them from low to high
top10 = sorted(items[:10], key=lambda item: item[1])
keys = [k for k,v in top10]
values = [v for k,v in top10]

# make the bar graph and save it as a png
plt.bar(keys, values)
if args.input_path.endswith('.lang'):
    label = 'Language' 
else:
    label = 'Country' 
plt.xlabel(label)
plt.ylabel('Number of tweets')
plt.title(args.key + ' by ' + label)
plt.tight_layout()
plt.savefig(os.path.basename(args.input_path) + '_' + args.key.lstrip('#') + '.png')

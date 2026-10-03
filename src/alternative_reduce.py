#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags',nargs='+',required=True)
parser.add_argument('--output_path',default='alternative_reduce.png')
args = parser.parse_args()

# imports
import os
import json
import datetime
import matplotlib.pyplot as plt

# scan the outputs folder and count how many tweets used each hashtag on each day
counts = {hashtag: {} for hashtag in args.hashtags}
for filename in sorted(os.listdir('outputs')):
    if not filename.endswith('.lang'):
        continue

    # file names look like geoTwitter20-01-01.zip.lang, so the date is characters 10 to 18
    date = datetime.datetime.strptime(filename[10:18], '%y-%m-%d')
    day = date.timetuple().tm_yday

    with open(os.path.join('outputs', filename)) as f:
        tmp = json.load(f)

    # add up the counts over all languages to get the total for that day
    for hashtag in args.hashtags:
        counts[hashtag][day] = sum(tmp.get(hashtag, {}).values())

# make the line plot, one line per hashtag
for hashtag in args.hashtags:
    days = sorted(counts[hashtag])
    values = [counts[hashtag][day] for day in days]
    plt.plot(days, values, label=hashtag)
plt.xlabel('Day of the year (2020)')
plt.ylabel('Number of tweets')
plt.title('Tweets per day using different #s')
plt.legend()
plt.tight_layout()
plt.savefig(args.output_path)

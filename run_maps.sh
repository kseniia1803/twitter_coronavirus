#!/bin/bash

mkdir -p outputs

for file in /data/Twitter\ dataset/geoTwitter20-*.zip
do
    name=$(basename "$file")
    nohup python3 src/map.py --input_path "$file" > "outputs/$name.log" 2>&1 &
done

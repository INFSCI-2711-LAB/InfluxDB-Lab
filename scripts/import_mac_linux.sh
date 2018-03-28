#!/bin/bash

current_dir=$(pwd)/$(dirname $0)

files=`ls $current_dir/../data/*.txt`
for filename in $files
do
	datetime="`date +%Y/%m/%d\ %H:%M:%S`"
    echo "$datetime Processing file: $filename"
    influx -import -path=$filename -precision=h -database=air
done
#!/usr/bin/bash
echo 'enter the directory address with a / at the end:'
read adrs
mkdir $adrs/copied
listf=$(find $adrs -mindepth 1 -maxdepth 1 -type f -name "*a*")
for f in $listf
do
	tx=$(cat $f)
	if [[ $tx = *[[:ascii:]]* ]]; then
	cp $f $adrs/copied
	fi
done
echo 'These files copied:'
ls $adrs/copied

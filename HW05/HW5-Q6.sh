#!/usr/bin/bash
echo 'enter the directory address with a / at the end:'
read adrs
touch newfile.txt
lista=$(ls $adrs)
for f in $lista
do
	name=$adrs/$f
	if [ -f "$name" ] ; then
		cat $adrs/$f >> $adrs/newfile.txt
	fi
done

head -10 $adrs/newfile.txt | tail -5 $adrs/newfile.txt

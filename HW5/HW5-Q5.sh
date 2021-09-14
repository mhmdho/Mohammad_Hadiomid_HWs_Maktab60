#!/usr/bin/bash
echo 'enter the directory address with a / at the end:'
read adrs
echo 'number of files are:'
find $adrs -mindepth 1 -maxdepth 1 -type f | wc -l

echo 'number of folders are:'
find $adrs -mindepth 1 -maxdepth 1 -type d | wc -l

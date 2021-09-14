#!/usr/bin/bash
echo 'enter the directory name:'
read dirname
if [ -d $dirname ]; then
	echo 'This directory exist'
else
	echo 'Directory not exist, it is created'
	mkdir $dirname
fi

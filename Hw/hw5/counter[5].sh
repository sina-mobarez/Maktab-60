#! /usr/bin/sh
# get a directory and count files & folders
echo "enter your directory"
read Directory
cd $Directory
x=`ls -l | grep '^-' | wc -l`
y=`ls -l | grep '^d' | wc -l`
echo "number of files are : $x "
echo "number of folders are : $y "
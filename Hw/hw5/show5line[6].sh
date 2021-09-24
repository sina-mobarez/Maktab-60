#! /usr/bin/sh
# get a directory from user
echo "enter your directory"
read Directory
cd $Directory
# get just files name by ls  command
x=`ls -p | egrep -v /$`
echo $x
# make a new file
touch newfile.txt
cat $x >> newfile.txt
head -n 10 newfile.txt | tail -n 5

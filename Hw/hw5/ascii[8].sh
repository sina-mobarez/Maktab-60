#! /usr/bin/sh
# get a directory from user
echo "enter your directory"
read Directory
cd $Directory
echo " enter another directory for copy files"
read SecondDir
# get just files name that contain "a" by ls  command
x=`ls -p | egrep -v /$ | grep 'a'`
# check file is ascii text and copy it into a new file
for file in $x
do
  if file $file | grep ASCII
  then
    cp -p $file $SecondDir
  fi
done

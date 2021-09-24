#!/usr/bin/sh
# get a directory from user
echo "enter a directory plz :"
read Directory
if [ -d $Directory ]
then
  echo "this directory already exist"
else
  mkdir $Directory
fi

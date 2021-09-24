#! /usr/bin/sh
# get a directory and show just files and if you don't give that show current directory files
echo "enter a directory"
read Directory
if [ -z "$Directory" ]
then
  cd $(pwd)
else
  cd $Directory
fi
ls -l | grep '^-' | wc -l

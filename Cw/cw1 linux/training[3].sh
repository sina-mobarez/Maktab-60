#! /usr/bin/sh
# get a directory and show just folders and if you don't give that show current directory folders
echo "enter a directory"
read Directory
if [ -z "$Directory" ]
then
  cd $(pwd)
else
  cd $Directory
fi
ls -l | grep '^d'

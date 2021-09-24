#! /usr/bin/sh
# get a directory and if it is folder show list dir and not show more it
echo "enter a directory"
read Directory
if [ -d "$Directory" ]; then
  echo $(ls $Directory)
elif [ -f "$Directory" ]; then
  more "$Directory"
else
  echo "Directory is not exist"
fi
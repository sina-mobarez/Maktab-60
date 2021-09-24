#! /usr/bin/sh
# get a word and show all of things that have it inside their name
echo "enter a directory"
read Path
echo "enter a word"
read Word
cd $Path
ls | grep $Word
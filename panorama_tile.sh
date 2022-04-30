#!/bin/bash

# Script that will cut a (wide) photo into 3 tiles, for example for creating
# a display on Instagram.

filename=`echo "${1%%.*}"`

convert -crop 3x1@ $1 "$filename"_tile_%d.jpg


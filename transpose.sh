#!/bin/bash

string=''
for x in `cat $1`
do
string="$string,$x"
done
echo $string | cut -c2-

#!/bin/bash

filename=$1

if [ -f $filename ]; then
    echo "File exists"
else
    echo "File does not exist"
fi

# Run the script

python3 $filename < ./p1_test1.dat
python3 $filename < ./p1_test2.dat
python3 $filename < ./p1_test3.dat

#!/bin/bash

dir=$1
cd $dir
cp ../testing/shapes_tester.py .
python3 shapes_tester.py
rm shapes_tester.py
python3 vehicle_collection.py < ../testing/input1.dat

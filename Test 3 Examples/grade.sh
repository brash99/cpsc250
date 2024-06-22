#!/bin/bash

dir=$1
cd $dir
cp ../testing/input1.dat .
cp ../testing/shapes_tester.py .
python3 shapes_tester.py
python3 vehicle_collection.py < input1.dat

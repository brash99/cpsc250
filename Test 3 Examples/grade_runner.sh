#!/bin/bash

# Get list of directories

# Loop through directories and run the grade script
# for each directory
#
# For example, if the directories are:
#  - student1
#  - student2
#  - student3
#
#  The script should run the grade script for each
#
#  ./grade.sh student1
#  ./grade.sh student2
#  ./grade.sh student3

# Get list of directories
for dir in $(ls -d */)  
do
  # Remove the trailing slash
  dir=${dir%*/}
  # Run the grade script
  echo "========================================="
  echo "Grading $dir"
  ./grade.sh $dir
  echo "=========== Finished ===================="
done
```

#!/bin/sh
# Verify whenever you are working from the corrected passed directory

# Help Function
Help()
{
  echo 'Verify whenever you are working from the corrected passed directory'
}

# Switch Options
while getopts ":h" option; do
  case $option in
    h) # Display Help
      Help
      exit;;
    \?) # Incorrect Option
      echo "Error: Invalid option"
      exit;;
  esac
done

dirname=`basename ${pwd}`
if [ ! ${dirname} = "build-util" ]
        then
        echo "Must run from build-util folder"
        exit 1
fi
#!/bin/bash

# Define the directory containing the text files
directory="."

# Define the output file
outfile="working_scripts.txt"

# Concatenate all text files starting with 'p' into the output file
cat "${directory}/p"* > "${outfile}"

echo "Concatenation complete. Output saved to ${outfile}"


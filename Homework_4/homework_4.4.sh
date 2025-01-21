#!/bin/bash

##############################
# Homework_4/Task_4
#
# Author: Andrei Dzyakanchuk
# Date: 16.01.2025
##############################

# set -x
# Line input
read input_string
# Highlight substring
hgl_substring=$input_string |  grep '[^a-zA-Z]'
# Define index of symbols
for index in "line";do
	echo -e "$index\n"
done


# Delete substring
#del_substring
# Print result
#echo $ext_substring


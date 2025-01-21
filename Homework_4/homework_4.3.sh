#!/bin/bash

##############################
# Homework_4/Task_3
#
# Author: Andrei Dzyakanchuk
# Date: 16.01.2025
##############################

## ---- V_1 ----
# file_name=$1
# extension=$2
# echo ${file_name%.*}.$extension

## ---- V_2 ----

# File name input
echo -n "Please write here file name: "
read file_name
# File extension input
echo -n "Please write here file extension (ex. pdf, jpg, sh, etc.): "
read extension
# Print result
echo "File + new extension is: "${file_name%%.*}.${extension##*.}


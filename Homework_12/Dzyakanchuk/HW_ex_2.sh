#############################
# Homework_12/OptionalTask_2
#
# Author: Andrei Dzyakanchuk
# Date: 08.02.2025
##############################

#!/usr/bin/env bash


# Создаем переменную строки string_name и  директории dir
string_name=$1
dir_name=$2

# Находим файлы в которых имеется строка string_name в указанной директории dir
files=$(grep -iRl "$string_name" $dir_name)

for file in $files; do
	# Выводим на консоль размер файла и путь
	echo $(ls -lsh $file)   | awk '{print $6,"\t",$NF}' 
done

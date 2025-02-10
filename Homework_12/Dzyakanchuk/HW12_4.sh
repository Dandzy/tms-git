##############################
# Homework_12/Task_4
#
# Author: Andrei Dzyakanchuk
# Date: 08.02.2025
##############################

#!/usr/bin/env bash

# Создаем переменные из вводимых аргументов
file_name=$1
dir=$2
extension=$3

#Создаем файл
touch $file_name

# Выводим список всех файлов в указанной директории dir и сохраняем в переменной files
files=$(find $dir -type f)

# Вызываем цикл и записываем все файлы с указанным расширением extension в файл file_name
for file in  $files; do
	file_extension=${file##*.}
	if [ "$file_extension" == "$extension" ]; then
		echo ${file##*/} >> $file_name		
	fi
done



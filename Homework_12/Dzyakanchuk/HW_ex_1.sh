##############################
# Homework_12/OptionalTask_1
#
# Author: Andrei Dzyakanchuk
# Date: 08.02.2025
##############################

#!/usr/bin/env bash

# Создаем переменные с директорией dir и списком файлов в заданной директории files соответственно
dir=$1
files=$(find $dir -type f)



for file in $files; do
        
	#Сохраняем имена файлов	
	file_name=${file##*/}
	# Выводим столбец размера файла и столбец прав доступа файла
	mem_and_rights=$(ls -lahs $file  | awk '{print $1,"\t", $2}')
	
        #Выводим в консоль
	echo $mem_and_rights $file_name
done




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

if [ $# -eq 0 ]; then
	echo "No arguments"
	exit 1
fi


if [ ! -d $dir ]; then
	echo "Wrong directory"
	exit 1
fi


echo -e "Mem\tAccess Mode\tFile_name"
for file in $files; do
        
	#Сохраняем имена файлов	
	file_name=${file##*/}
	
	# Выводим столбец размера файла и столбец прав доступа файла
        
	mem_and_perm=$(ls -lahs $file | awk '{print $6 "\t" $2}')
	
        #Выводим в консоль
	echo -e "$mem_and_perm\t$file_name"
done




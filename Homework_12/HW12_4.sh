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


# Проверяем введенные аргументы
if   [ $# -eq 0 ]; then
	echo "No arguments"
	exit 1
elif [ $# -eq 1 ]; then
	echo "You entered 1st argument, please enter 2nd and 3rd arguments"
	exit 1
elif [ $# -eq 2 ]; then
	echo "You entered 1st and 2nd arguments, please enter 3rd argument"
	exit 1
fi

# Проверяем наличие данной директории
if [ ! -d $dir ];then
	echo "There is no directory"
	exit 1
fi
# Проверяем расширение 
if [[ $extension  =~ '^[0-9]+$' ]];then
	echo "Wrong extension character"
	exit 1
fi

# Очищаем существующий файл или создаем новый 
if [ -f $file_name ];then
	$(rm -rf $file_name)
else	
	touch $file_name
fi

# Выводим список всех файлов в указанной директории dir и сохраняем в переменной files
files=$(find $dir -type f)



# Вызываем цикл и записываем все файлы с указанным расширением extension в файл file_name
for file in  $files; do
	file_extension=${file##*.}
	if [ "$file_extension" == "$extension" ]; then
		echo ${file##*/} >> $file_name		
	fi
done


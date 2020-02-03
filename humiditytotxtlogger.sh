#!/bin/bash

user="werner"
psw="Scripting"
database="templogger"
query="select humidity from full order by ID DESC LIMIT 50"

OIFS="$IFS" ; IFS=$'\n' ; oset="$-" ; set -f

declare -a test_array

while IFS="$OIFS" read -a line
do

  test_array+=(${line[0]})

done < <(mysql  -u${user} -p${psw} ${database} -e "${query}")

unset test_array[0]

>humidityvalues.txt

for i in ${test_array[@]}
do
  echo $i >> humidityvalues.txt
done

python3 ./humidity_statistics.py



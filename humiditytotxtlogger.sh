#!/bin/bash

# defines values for db connection
user="werner"
psw="Scripting"
database="templogger"
query="select humidity from full order by ID DESC LIMIT 50"

# interfield seperator
OIFS="$IFS" ; IFS=$'\n' ; oset="$-" ; set -f

# array for storing values
declare -a test_array

# adds line for line to array from db
while IFS="$OIFS" read -a line
do

  test_array+=(${line[0]})

done < <(mysql  -u${user} -p${psw} ${database} -e "${query}")

# removes first array entry (name from column)
unset test_array[0]

#cleares file
>humidityvalues.txt

#append lines to .txt file
for i in ${test_array[@]}
do
  echo $i >> humidityvalues.txt
done

# executes python script for statistics
python3 ./humidity_statistics.py



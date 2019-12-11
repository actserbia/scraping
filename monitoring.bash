#!/bin/bash

ps -C node -o pid,%mem,vsz,size,rss,command

echo
echo enter PID
echo
read PID
echo

seconds_start=$(date +%s)
while true; do
seconds_current=$(date +%s)  
seconds_relative=$((seconds_current - seconds_start))

row="$seconds_relative $(ps -p $PID -o %mem=,vsz=,size=,rss=)"
  
# ps -p $PID -o pid=,%mem=,vsz= >> /tmp/mem.log
echo $row
echo $row >> mem.log.csv


sleep 5
done

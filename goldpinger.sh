#!/bin/sh

# Small utility script to run dhclient on machines that lose
# their network connection but not the Wi-Fi connection.
#
# This script is run after the connection has been setup the
# first time. For example run after a delay.
#
# Has to be run as root.
#
# ./goldpinger.sh [timeout] [reboot command]
#
# timeout follows the format of sleep
#
# Will run reboot command after 30 consecutive failed ping commands

if [ ! -z "$1" ]; then
  /bin/sleep $1
fi
count="0"
if [ -z "$2" ]; then
  reboot="/sbin/reboot"
else
  reboot=$2
fi


# Getting the active interface
interface=`route|grep default|awk '{print $8}'`
while :
do
  ping -c 3 8.8.8.8 > /dev/null 2>&1
  if [ $? -eq 0 ];
  then
    count=0
  else
      count=`expr $count + 1`
      # Off by one?
      if [ $count -gt 30 ]; then
        echo "Rebooting.."
        (/bin/sleep 5s && $reboot) &
        exit 1
      fi
    echo `date -Iseconds` "Ping failed, regetting IP with dhclient"
    /sbin/dhclient $interface
  fi
  sleep 10s
done

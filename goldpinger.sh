#!/bin/sh

# Small utility script to run dhclient on machines that lose
# their network connection but not the Wi-Fi connection.
#
# This script is run after the connection has been setup the
# first time. For example run after a delay.
#
# Has to be run as root.

# Getting the active interface
interface=`route|grep default|awk '{print $8}'`
while :
do
  ping -c 3 8.8.8.8 > /dev/null 2>&1
  if [ $? -eq 0 ];
  then
    :
  else
    echo "Ping failed, regetting IP with dhclient"
    /sbin/dhclient $interface
  fi
  sleep 10s
done

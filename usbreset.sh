#!/bin/sh
#
# Simple script that will reset the USB system
#
# ./usbreset.sh [timeout]
#
# timeout is time between buses are taken down and brought back up again,
# default is 1 second.  Follows the format for sleep.

buses=`lspci|grep USB|awk '{print $1}'`

for bus in $buses
do
  echo -n 0000:$bus > /sys/bus/pci/drivers/ehci-pci/unbind
done

if [ ! -z "$1" ]; then
  /bin/sleep $1
fi

for bus in $buses
do
  echo -n 0000:$bus > /sys/bus/pci/drivers/ehci-pci/bind
done

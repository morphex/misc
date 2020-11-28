#!/bin/sh
#
# Script that will force a reboot, regardless of the state of things.  Only
# tries to synchronize the file systems, wait 5 seconds, then remount
# all file systems read only, wait 5 seconds, then reboot.
#
# Should be safe to setuid root.
#
# ./forcereboot.sh [timeout]
#
# timeout follows the format of sleep

if [ ! -z "$1" ]; then
  /bin/sleep $1
fi
# Try to synchronize filesystem state
/bin/sync &
sync_pid=$!
/bin/sleep 5s
# Remount all mounted filesystems read only
echo u > /proc/sysrq-trigger
/bin/sleep 5s
# Force an immediate reboot
/sbin/reboot -ff

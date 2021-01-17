#!/usr/bin/env python3

import os, sys

MINIMUM_UPTIME = 30 # 30 minutes
REBOOT_COMMAND = "/sbin/reboot"

def print_syntax():
    print(str(sys.argv[0]) + ' <logfile> <trigger> [minutes since boot] [reboot command]')

try:
    logfile = sys.argv[1]
    trigger = sys.argv[2]
except IndexError:
    print_syntax()
    sys.exit(1)
try:
    MINIMUM_UPTIME = int(sys.argv[3])
    REBOOT_COMMAND = sys.argv[4]
except IndexError:
    print_syntax()
    sys.exit(1)
except ValueError:
    print_syntax()
    sys.exit(1)

MINIMUM_UPTIME *= 60

data = open(logfile, 'r', errors='surrogateescape').read()
if data.find(trigger) > -1:
  uptime = float(open('/proc/uptime').read().split()[0])
  if uptime > MINIMUM_UPTIME:
    print('Reboot!')
    os.system('(/bin/sleep 5s && %s) &' % REBOOT_COMMAND)

#!/usr/bin/env python3

import os, sys

MINIMUM_UPTIME = 30 # 30 minutes

try:
    logfile = sys.argv[1]
    trigger = sys.argv[2]
except IndexError:
    print(str(sys.argv[0]) + ' <logfile> <trigger> <minutes since boot>')
    sys.exit(1)
try:
    MINIMUM_UPTIME = int(sys.argv[3])
except IndexError:
    pass

MINIMUM_UPTIME *= 60

data = open(logfile, 'r', errors='surrogateescape').read()
if data.find(trigger) > -1:
  uptime = float(open('/proc/uptime').read().split()[0])
  if uptime > MINIMUM_UPTIME:
    print('Reboot!')
    os.system('/sbin/reboot')

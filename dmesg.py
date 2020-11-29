#!/usr/bin/python3

__doc__ = """

Small utility script that will log the contents output by dmesg to a file.

./dmesg.py [append]

The option append will make the script only append to /var/log/dmesg.log,
without it, the script will also rotate and compress log files.

"""

import glob, os, sys

def sorting(a):
  return int(a.split('.')[2])

def increment_filename(filename):
  number = int(filename.split('.')[2])
  number += 1
  return "/var/log/dmesg.log." + str(number) + ".gz"

try:
  append = sys.argv[1]
  append = append == 'append'
except IndexError:
  append = False

if not append:
  dmesg_files = glob.glob("/var/log/dmesg.log.*.gz")
  if len(dmesg_files) > 0:
    dmesg_files = sorted(dmesg_files, key=sorting, reverse=True)
    print(dmesg_files)
    for filename in dmesg_files:
      os.rename(filename, increment_filename(filename))
  dmesg_file_old = glob.glob("/var/log/dmesg.log.0")
  if dmesg_file_old:
    os.rename("/var/log/dmesg.log.0", "/var/log/dmesg.log.1")
    os.system("gzip -9 /var/log/dmesg.log.1")
  dmesg_file = glob.glob("/var/log/dmesg.log")
  if dmesg_file:
    os.rename("/var/log/dmesg.log", "/var/log/dmesg.log.0")
os.system("dmesg -cHPT >> /var/log/dmesg.log 2>&1")
os.system("/bin/sync")

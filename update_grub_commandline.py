#!/usr/bin/env python3
#
# Script to add command line arguments to the Linux Kernel via GRUB on Ubuntu.
#
#
# For example
#
# ./update_grub_commandline.py maxcpus=2

import sys
grub_default_location='/etc/default/grub'

lines = open(grub_default_location, 'r').readlines()
new_lines = []
for line in lines:
    if line.startswith('GRUB_CMDLINE_LINUX_DEFAULT'):
        head, tail = line.split('=', 1)
        tail = tail.strip()
        tail = tail[1:-1]
        for argument in sys.argv[1:]:
            tail = tail + (" %s" % argument)
        line = head + '="' + tail + '"\n'
    new_lines.append(line)
new_file_content = ''.join(new_lines)
writer=open(grub_default_location, 'w')
writer.write(new_file_content)
writer.flush()
writer.close()

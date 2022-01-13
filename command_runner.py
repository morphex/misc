#!/usr/bin/python3

# Small script that will run command N number of times,
# sleeping S seconds between each run.  S can be a float,
# for example 0.1 (1 10th of a second).
#
# If N times is zero, repeat "forever".
#
# For example, repeat 10 times 2 seconds apart:
#
# ./command_runner.py 10 2 ls
#
# Loops forever, 2 seconds apart:
#
# ./command_runner.py 0 2 ls

import sys, os, time, itertools

if len(sys.argv) < 4:
    print("command_runner <N times> <S sleep> <command> [command argument 1, 2, ...]")
    sys.exit(1)
times = int(sys.argv[1])
if times == 0:
    repeater = itertools.repeat(1)
else:
    repeater = itertools.repeat(1, times=times)
sleep = float(sys.argv[2])
command = ' '.join(sys.argv[3:])
for x in repeater:
    os.system(command)
    time.sleep(sleep)

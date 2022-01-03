#!/usr/bin/python3

# Small script that will run command N number of times,
# sleeping seconds between each run.  N can be a float,
# for example 0.1 (1 10th of a second).

import sys, os, time

if len(sys.argv) < 4:
    print("command_runner <N times> <sleep> <command> [command argument 1, 2, ...]")
    sys.exit(1)
times = int(sys.argv[1])
sleep = float(sys.argv[2])
command = ' '.join(sys.argv[3:])
for x in range(0, times):
    os.system(command)
    time.sleep(sleep)

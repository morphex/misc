#!/bin/bash

# Small script that will turn laptop screen off when in console mode,
# press enter to turn screen back on.
#
# Requires vbetool to be installed ("apt install vbetool" on Debian /
# Ubuntu.

sudo mount -o remount,exec /dev
sudo sh -c "vbetool dpms off; read ans; vbetool dpms on"

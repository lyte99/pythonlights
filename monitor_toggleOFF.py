#!/usr/bin/python3
# coding: utf8 #

import subprocess  # for command execution

def myfunction():

	CONTROL = "vcgencmd" # command to turn the screen on
	CONTROL_UNBLANK = [CONTROL, "display_power", "0"] # command to turn the screen on
	subprocess.call(CONTROL_UNBLANK) # command to turn the screen on

myfunction()

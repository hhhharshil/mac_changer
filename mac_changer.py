#!/usr/bin/env python

import subprocess #usage of a library to exectute linux commands

interface = 'eth0' #usage of a var to declare eth0 
new_mac = '00:11:22:33:44:66' #usage of a var to declare the mac addy

print('[+] Changing Mac address for ' + interface + ' to ' + new_mac)

subprocess.call("ifconfig "+ interface + " down", shell=True)
subprocess.call("ifconfig "+ interface + " hw ether " + new_mac,shell=True)
subprocess.call("ifconfig "+ interface + " up", shell=True)
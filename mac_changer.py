#!/usr/bin/env python

import subprocess #usage of a library to exectute linux commands
import optparse #parse command line arguments from user.
import re #used to extract output using regex
logo = '''

 /$$   /$$ /$$   /$$ /$$   /$$ /$$   /$$                               /$$       /$$ /$$
| $$  | $$| $$  | $$| $$  | $$| $$  | $$                              | $$      |__/| $$
| $$  | $$| $$  | $$| $$  | $$| $$  | $$  /$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$  /$$| $$
| $$$$$$$$| $$$$$$$$| $$$$$$$$| $$$$$$$$ |____  $$ /$$__  $$ /$$_____/| $$__  $$| $$| $$
| $$__  $$| $$__  $$| $$__  $$| $$__  $$  /$$$$$$$| $$  \__/|  $$$$$$ | $$  \ $$| $$| $$
| $$  | $$| $$  | $$| $$  | $$| $$  | $$ /$$__  $$| $$       \____  $$| $$  | $$| $$| $$
| $$  | $$| $$  | $$| $$  | $$| $$  | $$|  $$$$$$$| $$       /$$$$$$$/| $$  | $$| $$| $$
|__/  |__/|__/  |__/|__/  |__/|__/  |__/ \_______/|__/      |_______/ |__/  |__/|__/|__/

'''
print(logo)

def arguments():
    parser = optparse.OptionParser() #object created 
    parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address") #added options to object
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[x] Please enter a valid interface, use --help for more information...")
    elif not options.new_mac:
        parser.error("[x] Please enter a valid MAC, use --help for more information...")
    return options 


def mac_change(interface, new_mac):      #function used to change mac address interface and new mac are retrieved using the options arg
    print('[+] Changing Mac address for ' + interface + ' to ' + new_mac)

    subprocess.call(["ifconfig", interface, "down"]) #we have a list here to prevent calling other commands rather than using the shell=True method
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w ", ifconfig_result) #using regex to search for the MAC Address string and returning its value

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print('[x] Could not read MAC Address')

options = arguments()

display_current_mac = current_mac(options.interface)
print('[+] Current MAC Address = ' + str(display_current_mac))
mac_change(options.interface, options.new_mac)
display_current_mac = current_mac(options.interface)
if display_current_mac == options.new_mac:
    print("[+] Mac Address was successfully changed to " + current_mac)
else:
    print("[x] Mac Address did not change")
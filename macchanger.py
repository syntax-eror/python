#!/usr/bin/env python

#MAC Address Changer from
#Learn Python and Ethical Hacking from Scratch course

#todo - convert to python3 (subprocess.call > subprocess.run)

import optparse #module for parsing options passed in from command line
import re #regular expression operator module
import subprocess #module for making calls to system (ex. ifconfig)

def change_mac(interface, newmac):
    print("[+] Changing MAC address for " + interface + " to " + newmac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newmac)
    subprocess.call(["ifconfig", interface, "up"])
	
def display_interfaces(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    #regular expression that searches for pattern of MAC address; aa:11:a1:f1:ee:11, etc
 
    if mac_address_search_result: #if this regex returns a result:
        return mac_address_search_result.group(0) #print it
	else: #otherwise there was an error with the search result
	    print("[-] Not able to locate MAC address for specified interface.")
		
def get_arguments():
    parser = optparse.OptionParser() #create parser object variable
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address of.")
    parser.add_option("-m", "--mac", dest="newmac", help="MAC address to change to.")
    (options, arguments) = parser.parse_args() #parses user input using parse_args, called from optparse, and stores them in two variables:
    #options and arguments
	if not options.interface:
	    parser.error("[-] Please specify an interface, use --help for more info.")
	elif not options.newmac:
	    parser.error("[-] Please specify a new MAC address, use --help for more info.")
	return options #returns whatever is parsed to the place that calls the function
	
options = get_arguments()

currentmac = display_interfaces(options.interface)

print("[+] MAC address of " + options.interface + " is " + str(currentmac))

change_mac(options.interface, options.newmac)

currentmac = display_interfaces(options.interface)

if currentmac == options.newmac:
    print("[+] MAC address for " + options.interface + " was changed to " + currentmac)
else:
    print("[-] MAC address for " + options.interface + " was NOT changed, check for errors and try again.")

#!/usr/bin/env python3

#MAC Address Changer from Learn Python and Ethical Hacking from Scratch course
#by Zaid Al-Quraishi

import optparse #module for parsing options passed in at command line
import re #regular expression operator module
import subprocess #module for making calls to system commands

def change_mac(interface, newmac):
    print("[+] Changing MAC address for", interface, "to", newmac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", newmac])
    subprocess.run(["ifconfig", interface, "up"])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address of")
    parser.add_option("-m", "--mac", dest="newmac", help="MAC address to change to")
    (options, arguments) = parser.parse_args()
    if not options.interface: #if no interface is given
        parser.error("[-] Please enter an interface, use --help for more information.")
        #parser.error is a function of OptionParser, will show error message you specify then exit
    elif not options.newmac: #if MAC address is not given
        parser.error("[-] Please enter the new MAC address, use --help for more information.")
    return options

#def troubleshooting(options, arguments): #temp function to try to help me understand what's going on in the program
def troubleshooting(options):
    print("Variable 'options' captured and is the type: ", type(options))
    #print("Variable 'arguments' captured and is the type: ", type(arguments))
    print("Variable 'options' equals:", options)
    #print("Variable 'arguments' equals:", arguments)


#(options, arguments) = get_arguments()
options = get_arguments()
troubleshooting(options)
change_mac(options.interface, options.newmac)

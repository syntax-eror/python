#!/usr/bin/env python3

#MAC Address Changer from Learn Python and Ethical Hacking from Scratch course
#by Zaid Al-Quraishi

import optparse #module for parsing options passed in from command line
import re #regular expression operator module
import subprocess #module for making calls to system commands

def change_mac(interface, newmac):
    print("[+] Changing MAC address for", interface, "to", newmac)
    subprocess.run(["ifconfig", interface])


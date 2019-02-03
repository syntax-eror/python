#!/usr/bin/env python3

import time

start_time = time.localtime()
print("Timer started at", time.strftime('%X', start_time))

input("Press enter to stop timer ")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print("Timer stopped at", time.strftime('%X', stop_time))
print("Time passed:", difference, " seconds.")

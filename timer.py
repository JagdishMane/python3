#!/usr/bin/env python3.6


import time
"""
 different kind of import statement
 from time import localtime, mktime, strftime
"""
start_time = time.localtime()
print(f"Time started at {time.strftime('%X', start_time)}" )

# Wait for user to stop timer
input("press 'Enter' to stop timer ")


stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print(f"Time Stoppped at {time.strftime('%X', stop_time)}" )
print(f"Total time: {difference} seconds")





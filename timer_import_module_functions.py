#!/usr/bin/env python3.6

from time import localtime, mktime, strftime

"""
 different kind of import statement
 from time import localtime, mktime, strftime
"""
start_time = localtime()
print(f"Time started at {strftime('%X', start_time)}" )

# Wait for user to stop timer
input("press 'Enter' to stop timer ")


stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Time Stoppped at {strftime('%X', stop_time)}" )
print(f"Total time: {difference} seconds")





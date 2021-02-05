import sys
import os
import re

error = input("What is the error? ")
returned_errors = []

def error_search(log_file):
    pattern = r'(CRON).*\s(ERROR: Failed to start)'


    with open(log_file) as file:
        for line in file:
            result = re.search(pattern, line)
            if result == None:
                continue
            returned_errors.append(line)
    return returned_errors


#print(error_search("/mnt/c/Users/eoliveira/Documents/projects/coursera/fishy.log"))
print(error_search("/Users/eoliveira/Documents/projects/coursera-1/fishy.log"))

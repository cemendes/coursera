import sys
import os
import re

def error_search(log_file):
    pattern = r'(CRON).*\s(ERROR: Failed to start)'
    returned_errors = {}

    with open(log_file) as file:
        for line in file:
            result = re.search(pattern, line)
            if result == None:
                continue
            returned_errors = {line}
    return returned_errors


print(error_search("/mnt/c/Users/eoliveira/Documents/projects/coursera/fishy.log"))

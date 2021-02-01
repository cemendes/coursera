#!/usr/bin/env python3

#Import libraries

import re
import csv

def contains_domain(address, domain):
    """Returns True if the email address contains the given domain,
    in the domain position, false if not."""
    domain_pattern = rf"([\w.-]+)@({domain})$"
    result = re.search(domain_pattern, address)
    if result != None:
        return True
    return False

def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in
    the received address."""

    old_username = re.sub(r"([\w\.-]+@)(.*)", r"\1", address)
    address = old_username+new_domain

    return address

def main():
    """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""
    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    # Define variable for the csv to be used all over the program.
    csv_file_location= '/Users/eoliveira/Documents/projects/coursera/user_emails.csv'
    report_file = '/Users/eoliveira/Documents/projects/coursera/update_user_emails.csv'
    csv_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file_location) as f:
        user_data_list = list(csv.reader(f))
        # data[1] = The second item of each sub-list. The first item is the full name and the second item is email address. 
        # user_data_list[1:] = Starts with the second list of the main list. user_data_list is a list of lists. 
        # Good explanation about list compreension. https://blog.teamtreehouse.com/python-single-line-loops
        user_email_list = [data[0] for data in user_data_list[1:]]
        # print(user_email_list)
        # print(user_data_list)
        # user_email_list = [data]
    for email_address in user_email_list:
        if contains_domain(email_address, old_domain):
            old_domain_email_list.append(email_address)
            replaced_email = replace_domain(email_address, old_domain, new_domain)
            new_domain_email_list.append(replaced_email)
    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)
    for user in user_data_list[1:]:
        for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
            if user[email_index] == ' ' + old_domain:
                user[email_index] = ' ' + new_domain
    f.close()
    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()
main()
# print(contains_domain("dudu@xuxu.com", "eu.com"))
# print(replace_domain("dudu@abc.edu", "abc.edu", "xuxu.com"))
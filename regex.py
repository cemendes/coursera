#region
# import re
# def check_web_address(text):
#   pattern = r"^[\w\.\-\+]*.[A-Za-z0-9]{2,3}$"
#   result = re.search(pattern, text)
#   return result != None

# print(check_web_address("gmail.com")) # True
# print(check_web_address("www@google")) # False
# print(check_web_address("www.Coursera.org")) # True
# print(check_web_address("web-address.com/homepage")) # False
# print(check_web_address("My_Favorite-Blog.US")) # True
# print(check_web_address("My_Favorite-Blog.K12")) # True

# import re
# def check_time(text):
#   pattern = r"[1-9]?[0-9]:[0-5][1-9]\s?(AM|PM|am|pm)"
#   result = re.search(pattern, text)
#   return result != None

# print(check_time("12:45pm")) # True
# print(check_time("9:59 AM")) # True
# print(check_time("6:60am")) # False
# print(check_time("five o'clock")) # False

# import re
# def contains_acronym(text):
#   pattern = r"\([A-Z0-9][A-Za-z0-9]*\)"
#   result = re.search(pattern, text)
#   return result != None

# print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
# print(contains_acronym("Please do NOT enter without permission!")) # False
# print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

# import re
# def transform_record(record):
#   new_record = re.sub(r"([0-9]{3}-)", r"+1-\1", record, count=1)
#   return new_record

# print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# # Sabrina Green,+1-802-867-5309,System Administrator

# print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# # Eli Jones,+1-684-3481127,IT specialist

# print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# # Melody Daniels,+1-846-687-7436,Programmer

# print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# # Charlie Rivera,+1-698-746-3357,Web Developer

# import re
# def multi_vowel_words(text):
#   pattern = r"\b\w*[a,e,i,o,u]{3}\w*\b"
#   result = re.findall(pattern, text)
#   return result

# print(multi_vowel_words("Life is beautiful")) 
# # ['beautiful']

# print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# # ['Obviously', 'queen', 'courageous', 'gracious']

# print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# # ['rambunctious', 'quietly', 'delicious']

# print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# # ['queue']

# print(multi_vowel_words("Hello world!")) 
# # []
# endregion

# import re
# def transform_comments(line_of_code):
#   result = re.sub(r"#+", r"//", line_of_code)
#   return result

# print(transform_comments("### Start of program")) 
# # Should be "// Start of program"
# print(transform_comments("  number = 0   ## Initialize the variable")) 
# # Should be "  number = 0   // Initialize the variable"
# print(transform_comments("  number += 1   # Increment the variable")) 
# # Should be "  number += 1   // Increment the variable"
# print(transform_comments("  return(number)")) 


# import re
# def convert_phone_number(phone):
#   result = re.sub(r"([0-9]{3})-([0-9]{3})-([0-9]{4}\.*)$", r"(\1) \2-\3", phone, count=1)
#   return result

# print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
# print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
# print(convert_phone_number("123-123-12345")) # 123-123-12345
# print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

import re
def show_time_of_pid(line):
  pattern = r'(\w{3}) ([0-9]+ [0-9]+:[0-9]+[0-9]+:[0-9]+) .*\[(\d+)'
  result = re.search(pattern, line)
  return result[1] + " " + result[2] + " " + "pid:" + result[3]
  # print(result[2])
  

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440
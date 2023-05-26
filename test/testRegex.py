import re

string_to_check = """● detector.service - Detector Service
   Loaded: loaded (/etc/systemd/system/detector.service; disabled; vendor preset: enabled)
   Active: inactive (dead)
"""

print(string_to_check)
# pattern = re.compile(r'^.*Active: (.*?) .*$', flags=re.MULTILINE)
pattern = re.compile(r"Active:.([a-z]*)", flags=re.MULTILINE)

matches = pattern.search(string_to_check)

print(matches[1])

# print(matches2)

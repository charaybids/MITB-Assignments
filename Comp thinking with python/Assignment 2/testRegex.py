import re

regex_pattern = r'(a).\n(t).'
search_string = 'abc\ngar\ntvd'


p = re.compile(regex_pattern)
outputRegex = p.findall(search_string)

print(outputRegex) # ['abc', 'a', 't']
#^\w(.)\n\w(.)\n\w(.)

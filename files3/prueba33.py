line = 'asdf fjdk; afed, fjek,asdf, foo'

import re
re.split(r'[;,\s]\s*', line)

fields = re.split(r'(;|,|\s)\s*', line)
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)


# in verbose mode, white space and new lines are ignored so you can split up your regex into multiple lines

import re

re.compile(r'''
(\d\d\d-) |         #area code (without parens, with dash)
(\(\d\d\d\))  )     #-or- area code with parens and no dash
\d\d\d              # first 3 digits
-                   # second dash
\d\d\d\d            # last 4 digits
''', re.VERBOSE)


# adding multiple flags as the 2nd argument into the compile function
# re.IGNORECASE | re.DOTALL | re.VERBOSE
#! python3

import re, pyperclip

# Copy the text from the arkanasas_directory, then run the app

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, 555-0000 ext. 12345, 555-0000 x12345
(                               # make the entire regex one group
((\d\d\d) | (\(\d\d\d\)))       # area code(optional)
(\s|-)                          # first separator
\d\d\d                          # first 3 digits
-                               # separator
\d\d\d\d                        # last 4 digits
(((ext(\.)?\s)|x) 
(\d{2,5}))?
)           # extension(option .) followed by 2-5 digits
''', re.VERBOSE)

# Create a regex for emails
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+         # range of characters that could be before the @
@                       #@
[a-zA-Z0-9_.+]+         # range of characters that could be after the @ and before .com


''', re.VERBOSE)


# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)



print(results)


# copy the extracted email/phone to the clipbaord
import webbrowser, sys, pyperclip

# command line arguments are accessed via sys.argv delimited by spaces
# ['webbrowser.py', '870', 'valencai', 'st.']

# if arguments were passed:
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# 'https://www.google.com/maps/place/870+Valencia+St,+San+Francisco,+CA+94110'


webbrowser.open('https://www.google.com/maps/place/' + address)


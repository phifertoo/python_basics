# pip isntall imapclient
# pip installl pyzmail36

import imapclient
import pyzmail
from gmail_pass import gmail_pass


conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

conn.login('jasonleezurich@gmail.com', gmail_pass)

conn.select_folder('INBOX', readonly=True)

# returns the UID's of messages sent 8/17/20 or later
# other imap search criteria: 'ALL', 'BEFORE date', 'SUBJECT string', 'BODY string', 'TEXT string'
UIDs = conn.search(['SINCE', '17-AUG-2020'])
# fetch the raw message([UID], ['BODY[]', 'FLAGS'])
raw_message = conn.fetch([5], ['BODY[]', 'FLAGS'])
# extract the message using PyzMessage
message = pyzmail.PyzMessage.factory(raw_message[5][b'BODY[]'])

subject = message.get_subject()
sender = message.get_address('from')
addressee = message.get_addresses('to')

# extract the text
output = message.text_part.get_payload().decode('UTF-8')

# to determine what type of decoding to use
decoding = message.text_part.charset

# list folders
conn.list_folders()

# delete emails / SET READONLY TO FALSE
# conn.select_folder('INBOX', readonly = False)
# conn.delete_messages([4])

conn.logout()

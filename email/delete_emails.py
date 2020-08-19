
import imapclient
import pyzmail
from gmail_pass import gmail_pass

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# returns the UID's of messages sent 8/17/20 or later
# other imap search criteria: 'ALL', 'BEFORE date', 'SUBJECT string', 'BODY string', 'TEXT string'
UIDs = conn.search(['SINCE', '17-AUG-2020'])

conn.select_folder('INBOX', readonly = False)
# [UID]
conn.delete_messages([4])
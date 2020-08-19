# you can send a maximum of 500 emails per day
import smtplib
from gmail_pass import gmail_pass

# pass in the SMTP email server and pass in the port number
conn = smtplib.SMTP('smtp.gmail.com', 587)

# connect to the email server
conn.ehlo()

# start tls encryption
conn.starttls()

# login
conn.login('jasonleezurich@gmail.com', gmail_pass)

# from email, to email, 'Subject: .....\n\n...body...""
conn.sendmail('jasonleezurich@gmail.com', 'phiferthree@gmail.com', 'Subject: my_title\n\nhello from my first email\n\n-from myself')

conn.quit()
# import required libraries
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
from PIL import Image
  
# use your email id here
username = "imageeditor10atharva@gmail.com" 
  
# use your App Password you
# generated above here.
password = "Veda@spit" 
  
# creata a imap object
imap = imaplib.IMAP4_SSL("imap.gmail.com")
  
# login
result = imap.login(username, password)
  
# Use "[Gmail]/Sent Mails" for fetching
# mails from Sent Mails. 
imap.select('"[Gmail]/All Mail"', 
readonly = True) 
  
response, messages = imap.search(None, 
                                 'UnSeen')
messages = messages[0].split()
  
# take it from last
latest = int(messages[-1])
  
# take it from start
oldest = int(messages[0])
  
for i in range(latest, latest-20, -1):
    # fetch
    res, msg = imap.fetch(str(i), "(RFC822)")
      
    for response in msg:
        if isinstance(response, tuple):
  
           msg = email.message_from_bytes(response[1])
           # print required information
           print(msg["Date"])
           print(msg["From"])
           print(msg["Subject"])
  
    for part in msg.walk():
        if part.get_content_type() == "image/png":
            # get text or plain data
            body = part.get_payload(decode = True)
            print(type(body))
            # print(f'Body: {body.decode("UTF-8")}', )
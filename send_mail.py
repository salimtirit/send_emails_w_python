import ssl
import smtplib
from email import encoders
from email.mime.base import MIMEBase
import config

smtp_server = 'smtp.gmail.com'

port = 465

sender = config.sender
password = input('Enter your password:') #you can use this from config also
receiver = config.receiver

message = """\
From: {}
To: {}
Subject: Hi There!

I am sending this through mycode!
""".format(sender,receiver)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, context=context) as server:
    server.login(sender, password)
    
    server.sendmail(sender,receiver,message)


import ssl
import smtplib
import config

smtp_server = 'smtp.gmail.com'

port = 465

sender = config.sender
password = input('Enter your password:') #you can use this from config also

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, context=context) as server:
    server.login(sender, password)
    print("works")


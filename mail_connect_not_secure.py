import smtplib, ssl
import config

smtp_server = 'smtp.gmail.com'
port = 587 #important

sender = config.sender
password = input('Enter your password:') #you can use this from config also

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender,password)
    print('worked')
except:
    print('nah')
finally:
    server.quit()

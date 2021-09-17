import ssl
import smtplib
from email import encoders
from email.mime.base import MIMEBase

from email import message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

smtp_server = 'smtp.gmail.com'

port = 465

sender = config.sender
password = input('Enter your password:') #you can use this from config also
receiver = config.receiver

message = MIMEMultipart('alternative')

message['Subject'] = 'Multipart Test'
message['From'] = sender
message['To'] = receiver

text = """Hi, how are you?
Real python has many great tutorials but not free so fuck it
"""
html = """\
<!DOCTYPE html>

<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <title>This is going to be awesome!</title>
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
</head>

<body>
    <div id="as">

    </div>
</body>

</html>

"""

part1 = MIMEText(text)
part2 = MIMEText(html)

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, context=context) as server:
    server.login(sender, password)
    
    server.sendmail(sender,receiver,message.as_string())
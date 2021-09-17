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

<body>
    <div id="as">
        <h2>YOU</h2>
        <p> are the best</p>
    </div>
</body>

</html>

"""
part1 = MIMEText(text,"plain")
message.attach(part1)


part2 = MIMEText(html)

message.attach(part2)


context = ssl.create_default_context()

filename = 'var.xlsx'

with open(filename,'rb') as attachment:
    att = MIMEBase("application", "octet-stream")
    att.set_payload(attachment.read())

encoders.encode_base64(att)


att.add_header(
    "Content-Disposition",
    f"attachment; filename={filename}",
)


message.attach(att)




with smtplib.SMTP_SSL(smtp_server, context=context) as server:
    server.login(sender, password)
    
    server.sendmail(sender,receiver,message.as_string())

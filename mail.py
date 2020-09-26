import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = ""
receiver_email = ""
reply_email = ""
sender_name = ""

message = MIMEMultipart()
message["Subject"] = "Important annoucement"
message["From"] = f"{sender_name}<{sender_email}>"
message["To"] = receiver_email
message["Bcc"] = receiver_email
message['X-Priority'] = '1'
#3 Normal Priority
#1-2 High Priority
message.add_header('reply-to', reply_email)

# Create your HTML message
body = """\
<html>
  <body>
    <p>Hi,<br>
       This is a test phishing email<br>
       <a href="https://www.nist.gov/news-events/news/2018/06/youve-been-phished">Link</a>
    </p>
  </body>
</html>
"""

message.attach(MIMEText(body, "html"))
filename = "document.pdf"

with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

message.attach(part)
print(message)

# Create secure connection with server and send email
smtpObj = smtplib.SMTP('')
smtpObj.sendmail(sender_email, receiver_email, message.as_string())    

import csv
from decouple import Config, RepositoryEnv
import smtplib

# https://docs.python.org/3/library/email.html
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

config = Config(repository=RepositoryEnv('.env'))

# email sender and reciever
login = sender_email = config('EMAIL_HOST_USER')
receiver_email = "tomdu3@ymail.com"
password = config('EMAIL_HOST_PASSWORD')
# Message
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# write the text/plain part
text = """\
Hi,[Name]
Hello from:
Tomdu3 Website https://tomdu3.co.uk/

Feel free to connect!"""

# write the HTML part
html = """\
<html>
  <body>
    <p style="text-align: center;">Hi,[Name]<br>
      Hello from:</p>
    <p style="text-align: center;"><a href="https://tomdu3.co.uk"><span style="color: red;">Tomdu3</span> Website</a></p>
    <p style="text-align: center;"> Feel free to <strong>connect</strong>!</p>
  </body>
</html>
"""


# convert both parts to MIMEText objects and add them to the MIMEMultipart message
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# send your email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # start TLS encryption
    server.login(login, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )

print('Sent')

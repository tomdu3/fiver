from decouple import Config, RepositoryEnv
import smtplib
from email.utils import formataddr


# https://docs.python.org/3/library/email.html
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

config = Config(repository=RepositoryEnv('.env'))

# default settings
sender_name = config('SENDER_NAME')
login = sender_email = config('EMAIL_HOST_USER')
password = config('EMAIL_HOST_PASSWORD')


def send_email(receiver, receiver_email):

    # Message
    subject = lambda receiver: f"Happy birthday, {receiver}"

    message = MIMEMultipart("alternative")
    message["Subject"] = subject(receiver)
    message["From"] = formataddr((sender_name, sender_email))
    message["To"] = receiver_email

    # write the text/plain part
    text = lambda receiver: f"""\
    Hi,{receiver}
    I wish you all the best for your birthday.

    {sender_name}
    """

    # write the HTML part

    html = lambda receiver: """<html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Birthday Wishes</title>
    <style>
        body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 20px;
        }
        .container {
        max-width: 600px;
        margin: auto;
        background-color: #ffffff;
        border-radius: 8px;
        padding: 30px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
        color: #333333;
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
        }
        p {
        font-size: 16px;
        line-height: 1.5;
        color: #555555;
        margin: 0 0 20px 0;
        }
        .signature {
        margin-top: 30px;
        font-style: italic;
        color: #777777;
        }
    </style>
    </head>""" + f"""<body>
    <div class="container">
        <h1>Happy Birthday!</h1>
        <p>Hi, <strong>{receiver}</strong></p>
        <p>I wish you all the best for your birthday.</p>
        <p class="signature">{sender_name}</p>
    </div>
    </body>
    </html>
    """


    # convert both parts to MIMEText objects and add them to the MIMEMultipart message
    part1 = MIMEText(text(receiver), "plain")
    part2 = MIMEText(html(receiver), "html")
    message.attach(part1)
    message.attach(part2)

    # send your email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # start TLS encryption
        server.login(login, password)
        server.sendmail(
            formataddr((sender_name, sender_email)),
            formataddr((receiver, receiver_email)),
            message.as_string()
        )

    print('Sent:\n', part1)
